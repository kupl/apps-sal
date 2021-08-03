import re


def domain_name(url):
    match = re.search(r'(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url)
    return match.group('name')
