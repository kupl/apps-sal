import re


def domain_name(url):
    return re.search(r'(/{2})?(www\.)?(?P<name>[\w-]+)[.?]', url).group('name')
