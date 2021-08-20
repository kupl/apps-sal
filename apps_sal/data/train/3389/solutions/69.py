import re


def domain_name(url):
    return re.compile('(https:|http:)?(//)?(www.)?([\\w+-]+)').match(url).group(4)
