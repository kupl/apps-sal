def domain_name(url):
    for i in ['http://','https://','.com','www.']:url=url.replace(i,'')
    return url.replace('.','/').split('/')[0]

