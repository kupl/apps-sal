def domain_name(url):
    filter_list = ['http://', 'www.', 'https://']
    for f in filter_list:
        if f in url:
            url = url.replace(f, '')
    new_url = url.split('.')
    return new_url[0]
