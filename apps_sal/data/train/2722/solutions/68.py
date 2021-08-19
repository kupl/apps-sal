def remove_url_anchor(url):
    return ''.join(url.split('#')[:1])
