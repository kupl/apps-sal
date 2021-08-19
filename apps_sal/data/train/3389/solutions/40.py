def domain_name(url):
    url = url.replace('www.', '').replace('https://', '').replace('http://', '')
    index = url.find('.')
    return url[0:index]
    pass
