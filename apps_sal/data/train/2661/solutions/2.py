import re


def find_codwars(url):
    return re.search(r'^(https?://)?(www.)?([^/]+\.)?codwars\.com([/&?].*|\Z)', url) is not None
