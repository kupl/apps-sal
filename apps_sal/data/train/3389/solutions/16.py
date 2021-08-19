import re


def domain_name(url):
    print(url)
    ur = '(?:https?://www\\.|www\\.|https://www\\.|https?://|)(.+?)\\.'
    a = re.findall(ur, url)
    if len(a) == 0:
        return ''
    return a[0]
