def domain_name(url):
    return url.split('//')[-1].replace('www.', '').split('.')[0]
