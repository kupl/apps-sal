import re


def domain_name(url):
    r = re.sub(r'www\.', '', url)
    r = re.search(r'[\w\-]{3,}\.\w{2,3}', r)
    r = re.search(r'[\w\-]+', r[0])
    return r[0]
