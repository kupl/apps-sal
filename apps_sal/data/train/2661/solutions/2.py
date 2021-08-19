import re


def find_codwars(url):
    return re.search('^(https?://)?(www.)?([^/]+\\.)?codwars\\.com([/&?].*|\\Z)', url) is not None
