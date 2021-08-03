import re


def remove_url_anchor(url):
    match = re.search(r'[a-zA-Z0-9.?/=:]+', url)
    return match.group()
