import re


def remove_url_anchor(url):
    match = re.search('[^#]+', url)
    if match:
        return match.group()
    else:
        return url
