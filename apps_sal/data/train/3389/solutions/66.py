import re


def domain_name(url):
    return re.search('^(https?\\:\\/\\/)?(www.)?([a-zA-Z0-9\\-]+)', url).group(3)
