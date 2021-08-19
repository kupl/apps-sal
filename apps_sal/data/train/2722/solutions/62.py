import re


def remove_url_anchor(url):
    return re.match('(.+)#', url)[1] if '#' in url else url
