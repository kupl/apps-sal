def remove_url_anchor(url):
    l = url.split('#',1)
    return l[0]
