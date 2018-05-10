import collections
import re
import datetime

from collections import defaultdict


def calculate_word_frequency_stat(articles_info, min_word_len=3):
    words_weeks_list = []
    week_words = []

    lower_letters_regex = re.compile('[^a-zа-я]')

    current_date = datetime.datetime.now().date()
    last_date = articles_info[-1]['date']
    week_date = current_date - datetime.timedelta(days=7)
    if week_date < last_date:
        week_date = last_date
    for idx, article_info in enumerate(articles_info):
        article_date = article_info['date']
        words_string = '%s %s' % (
            article_info['title'],
            article_info['preview'],
        )
        words_string = words_string.lower().strip()
        current_words = lower_letters_regex.sub(
            ' ',
            words_string
        ).split()
        week_words += [w.strip() for w in current_words if w and len(w) >=
                       min_word_len]
        if article_date < week_date:
            week_date = article_date - datetime.timedelta(days=7)
            words_weeks_list.append(week_words)
            week_words = []
        elif idx + 1 == len(articles_info):
            words_weeks_list.append(week_words)
            week_words = []
    stat = {}
    for idx, words in enumerate(words_weeks_list):
        stat[idx] = {}
        stat[idx]['words'] = defaultdict(list)
        stat[idx]['words'] = collections.Counter(words).most_common()
        if not (idx + 1 == len(words_weeks_list)):
            stat[idx]['week'] = '{} - {}'.format(current_date, current_date -
                                                 datetime.timedelta(days=7))
        stat[idx]['week'] = '{} - {}'.format(current_date, last_date)
        current_date -= datetime.timedelta(days=7)

    return stat


def output_word_stat(word_stat, week, top_size=10):
    print(week)
    for word, repetitions_amount in word_stat[:top_size]:
        print('%s: %s' % (word, repetitions_amount))
