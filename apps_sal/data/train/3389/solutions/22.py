import re


def domain_name(url):
    pattern = r'^(https?://(www.)?|(www.))?([^.]+)\..*$'
    return re.sub(pattern, r'\4', url)
