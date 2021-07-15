def domain_name(url):
    if 'www.' in url:
        return url.split('.')[1].split('.')[0]
    elif '.' and '//' in url:
        return url.split('//')[1].split('.')[0]
    else:
        return url.split('.')[0]
