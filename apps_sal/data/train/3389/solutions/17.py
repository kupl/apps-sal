def domain_name(url):
    domain = url.replace('http://', '').replace('www.', '').replace('https://', '')
    domain1 = domain.split('.')
    return ''.join(domain1[0])
    

