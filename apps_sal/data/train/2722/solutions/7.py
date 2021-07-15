from urllib.parse import urldefrag
def remove_url_anchor(url):
    return urldefrag(url).url

