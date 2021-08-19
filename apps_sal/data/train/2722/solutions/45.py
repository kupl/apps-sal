import re


def remove_url_anchor(url):
    regex = '#\\w+.+'
    subst = ''
    result = re.sub(regex, subst, url)
    return result
