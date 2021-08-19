def domain_name(url):
    url = url.replace('http://www.', '')
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    return url[:url.index('.')]
