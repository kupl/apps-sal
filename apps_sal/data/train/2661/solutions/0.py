import re


def find_codwars(url):
    return bool(re.match('^(https?://)?([a-z]+\\.)*codwars\\.com([/?].*)?$', url))
