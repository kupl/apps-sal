def domain_name(url):
    if url[:4] == 'http' or url[:4] == 'www.':
        url = url[4:]
        if url[0] == 's':
            url = url[1:]
    if url[:3] == '://':
        url = url[3:]
    if url[:4] == 'www.':
        url = url[4:]
    dot = url.index('.')
    url = url[:dot]
    return url

