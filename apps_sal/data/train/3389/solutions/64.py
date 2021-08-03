def domain_name(url):
    if url[0:4] == 'http':
        url = url[url.find('//') + 2:-1]
    url = url.split('.')
    return url[0] if url[0] != 'www' else url[1]
