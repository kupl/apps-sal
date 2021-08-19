def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    last = url.rfind('/')
    if last is not None:
        url = url[:last]
    dot = url.find('.')
    if dot is not None:
        url = url[:dot]
    return url
