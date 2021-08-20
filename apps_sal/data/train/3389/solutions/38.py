def domain_name(url):
    url = url.split('www.')[-1]
    url = url.split('//')[-1]
    url = url.split('.')[0]
    return url
