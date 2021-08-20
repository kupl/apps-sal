def domain_name(url):
    parts = url.split('//')
    portion = parts[0]
    if len(parts) > 1:
        portion = parts[1]
    if 'www' in portion:
        return portion.split('.')[1]
    return portion.split('.')[0]
