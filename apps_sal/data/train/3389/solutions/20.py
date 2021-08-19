import re


def domain_name(url):
    return re.match('(?:https?\\://)?(?:www.)?([a-z0-9-]*)\\.*', url).group(1)
