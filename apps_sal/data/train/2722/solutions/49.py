import re


def remove_url_anchor(url):
    urlRegex = re.compile('#(.*)')
    mo = str(urlRegex.sub('', url))
    return mo


print(remove_url_anchor('www.codewars.com/katas/'))
