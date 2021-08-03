import re


def domain_name(url):
    url_pattern = re.compile(r'^(https?://(www.)?|(www.))?([^.]+)\..*$')
    return url_pattern.sub(r'\4', url)
