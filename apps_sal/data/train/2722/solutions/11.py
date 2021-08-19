import re


def remove_url_anchor(url):
    return re.sub("#[a-zA-Z0-9]+$", "", url)
