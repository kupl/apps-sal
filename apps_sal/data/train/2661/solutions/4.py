import re


def find_codwars(url):
    return bool(re.match('(https?:\\/\\/)?(www\\.)?(\\w+\\.)*codwars\\.com(?=\\/|\\?|$)', url))
