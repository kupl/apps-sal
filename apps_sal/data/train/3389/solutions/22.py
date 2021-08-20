import re


def domain_name(url):
    pattern = '^(https?://(www.)?|(www.))?([^.]+)\\..*$'
    return re.sub(pattern, '\\4', url)
