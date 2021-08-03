def domain_name(url):
    if url.startswith('http'):
        url = url.split('//')[1]
    if url.startswith('www'):
        return(url.split('.')[1])
    return(url.split('.')[0])
