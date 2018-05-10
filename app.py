import argparse
import requests


def _fetch_page(url, pagination, page_num):
    url_with_page = url + pagination.format(page_num) + '/'
    return requests.get(url_with_page).text


def fetch_raw_pages(url, pagination, pages):
    raw_pages = []
    for page_num in range(pages):
        raw_pages.append(_fetch_page(url, pagination, page_num+1))
    return raw_pages


def main(args):
    print('Parsing {}'.format(args.s))
    url = args.s
    pages = args.p
    pagination = args.pag
    raw_pages = fetch_raw_pages(url, pagination, pages)
    print(raw_pages)




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
    args = parser.parse_args()
    print(args)
    main(args)
