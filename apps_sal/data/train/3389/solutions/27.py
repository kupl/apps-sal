from urllib.parse import urlparse


def domain_name(url):
    if not (url.startswith("https://") or url.startswith("http://")):
        url = "http://" + url
    return urlparse(url).hostname.replace("www.", "").split(".")[0]
