import re

def remove_url_anchor(url):
    fn = re.search(r"[^#]+", url)
    return fn.group(0)

