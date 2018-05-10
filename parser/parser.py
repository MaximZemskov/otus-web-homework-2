import bs4
import re
import datetime

_MONTHS = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}


def _get_date(day, month, time, year):
    month = _MONTHS[month]
    hours, minutes = time.split(':')
    date = datetime.datetime.strptime('{}-{}-{} {}:{}'.format(day, month, year,
                                                              hours,
                                                              minutes),
                                      "%d-%m-%Y "
                                      "%H:%M").date()
    return date


def parse_date(date_block):
    today_date = re.compile('^(сегодня\sв\s\w{2}:\w{2})$')
    yesterday_date = re.compile('^(вчера\sв\s\w{2}:\w{2})$')
    other_date = re.compile('^(\d+\s\w+\sв\s\w{2}:\w{2})')
    now = datetime.datetime.now()
    date_block_content = date_block.contents[0].strip()
    if today_date.match(date_block_content):
        date = now.date()
    elif yesterday_date.match(date_block_content):
        date = (now - datetime.timedelta(days=1)).date()
    elif other_date.match(date_block_content):
        day, month, time = date_block_content.strip().replace(' в ', ' ').split(" ")
        date = _get_date(day, month, time, now.year)
    else:
        day, month, year, time = date_block_content.strip().replace(' в ', ' ') \
            .split(" ")
        date = _get_date(day, month, time, year)
    return date


def parse_page(raw_page, title_class, article_class, article_block_class,
               time_block_class):
    articles_info = []
    soup = bs4.BeautifulSoup(raw_page, 'html.parser')
    for article_block in soup.find_all(
            'article',
            {'class': article_block_class},
    ):
        title_link = article_block.find('a', {'class': title_class})
        text_block = article_block.find('div', {'class': article_class})
        date_block = article_block.find('span', {'class': time_block_class})
        date = parse_date(date_block)
        articles_info.append({
            'title': title_link.contents[0],
            'preview': text_block.text.replace('\r\n', ''),
        })
    return articles_info
