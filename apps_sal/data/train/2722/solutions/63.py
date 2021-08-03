def remove_url_anchor(url):
    splt = url.split('#', 1)
    sub = splt[0]
    return sub
