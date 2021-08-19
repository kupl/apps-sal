import re


def domain_name(url):
    url_pattern = re.compile('^(https?://(www.)?|(www.))?([^.]+)\\..*$')
    return url_pattern.sub('\\4', url)
