import requests


def _fetch_page(url, pagination, page_num):
    url_with_page = url + pagination.format(page_num) + '/'
    return requests.get(url_with_page).text


def fetch_raw_pages(url, pagination, pages):
    raw_pages = []
    for page_num in range(pages):
        raw_pages.append(_fetch_page(url, pagination, page_num+1))
    return raw_pages
