import re


def remove_url_anchor(url):
    match = re.search('[a-zA-Z0-9.?/=:]+', url)
    return match.group()
