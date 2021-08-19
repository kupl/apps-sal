def domain_name(url):
    return url.replace('http://', '').replace('www.', '').replace('https://', '').replace('.', ' ').split()[0]
