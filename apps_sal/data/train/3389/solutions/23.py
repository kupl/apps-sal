import re


def domain_name(url):
    r = re.sub('www\\.', '', url)
    r = re.search('[\\w\\-]{3,}\\.\\w{2,3}', r)
    r = re.search('[\\w\\-]+', r[0])
    return r[0]
