import re

def find_codwars(url):
    return bool(re.match(r'(https?:\/\/)?(www\.)?(\w+\.)*codwars\.com(?=\/|\?|$)', url))
