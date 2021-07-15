def domain_name(url):
    if 'www.' in url:
        x = url.split('www.')
        url = x[1]
    if '://' in url:
        x = url.split('://')
        url = x[1]
    if '.' in url:
        x = url.split('.')
        x = x[0]
    return x
