def remove_url_anchor(url):
    s = '#'
    l = len(url)
    pos = url.find(s)
    if pos <= l and pos > 0:
        url = url[:l - (l - pos)]
    return url
