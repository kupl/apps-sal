def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    url = url.split('.')
    return url[0]
