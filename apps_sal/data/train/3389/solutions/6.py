import re


def domain_name(url):
    return re.search('(https?:\\/\\/)?(www\\d?\\.)?([\\w-]+)\\.', url).group(3)
