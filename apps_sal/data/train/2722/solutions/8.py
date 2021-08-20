import re


def remove_url_anchor(url):
    fn = re.search('[^#]+', url)
    return fn.group(0)
