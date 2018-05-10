import argparse

from parser.fetch import fetch_raw_pages
from parser.parser import parse_page
from parser.stat import calculate_word_frequency_stat, output_word_stat


def main(args):
    print('Parsing {}'.format(args.s))
    url = args.s
    pages = args.p
    pagination = args.pag
    raw_pages = fetch_raw_pages(url, pagination, pages)
    articles_info = []
    for raw_page in raw_pages:
        articles_info += parse_page(raw_page, title_class=args.tc,
                                    article_class=args.ac,
                                    article_block_class=args.ab,
                                    time_block_class=args.tb)
    word_stat = calculate_word_frequency_stat(
        articles_info
    )
    output_word_stat(word_stat)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '-site', help='Site address. Example: '
                                            'https://habr.com/all/')
    parser.add_argument('--p', '--pages', nargs='?', help='Numer of pages. \
        Default 10', const=10, default=10)
    parser.add_argument('--pag', '--pagination', nargs='?',
                        default='page{}/', help='Pagination uri. '
                                                'Example page{}/ or '
                                                '?page={} . Default '
                                                'page{}/')
    parser.add_argument('--tc', '--title_class', nargs='?',
                        default='post__title_link', help='CSS class of '
                                                         'title . Default: '
                                                         'post__title_link')
    parser.add_argument('--ac', '--article_class', nargs='?',
                        default='post__text', help='CSS class of '
                                                   'title . Default: '
                                                   'post__text')
    parser.add_argument('--ab', '--article_block', nargs='?',
                        default='post post_preview', help='CSS class of '
                                                          'article block . '
                                                          'Default: '
                                                          'post post_preview')
    parser.add_argument('--tb', '--time_block', nargs='?',
                        default='post__time', help='CSS class of '
                                                   'time block . '
                                                   'Default: '
                                                   'post__time')

    args = parser.parse_args()
    print(args)
    main(args)
