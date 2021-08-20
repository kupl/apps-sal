import re


def domain_name(url):
    return re.sub('(http(s)?:\\/\\/)?(www\\.)?', '', url).split('.')[0]
