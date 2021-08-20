def remove_url_anchor(url):
    if not '#' in url:
        return url
    return url[0:url.index('#')]
