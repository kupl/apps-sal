def domain_name(url):
    print(url)
    if '//' in url:
        url = url.split('//', 1)[1]
    if 'www.' in url:
        url = url.split('www.', 1)[1]
    return url.split('.', 1)[0]
