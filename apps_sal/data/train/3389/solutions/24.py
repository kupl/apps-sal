import re


def domain_name(url):
    domain = re.sub('(http[s]?://)?(www\.)?([^\.]+)(.*)', '\g<3>', url)
    return domain
