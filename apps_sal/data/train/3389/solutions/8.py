import re


def domain_name(url):
    return re.search('(/{2})?(www\\.)?(?P<name>[\\w-]+)[.?]', url).group('name')
