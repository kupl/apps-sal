def domain_name(url):
    if 'www.' in url:
        url = url.split('www.')[-1]
    elif '//' in url:
        url = url.split('//')[-1]
    return url.split('.')[0]
