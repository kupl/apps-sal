def domain_name(url):
    return url.replace('www.', '').replace('http:', '').replace('https:', '').replace('/', '').split('.')[0]
