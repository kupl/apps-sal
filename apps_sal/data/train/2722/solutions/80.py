import re


def remove_url_anchor(url):
    pattern = re.compile('^([^#]+)(#[.]*)*')
    m = re.match(pattern, url)
    return m.group(1)
