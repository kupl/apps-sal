def remove_url_anchor(url):
    idx = url.find('#')
    if idx == -1: return url
    return url[:idx]
