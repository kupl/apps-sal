import re


def remove_url_anchor(url):
    return re.search('^(.*?)(#|$)', url).group(1)
