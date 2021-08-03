def find_codwars(url):
    url = url.split('/')
    domain = url[0] if ':' not in url[0] else url[2]
    domain = domain.split('?')[0]
    domain = domain.split('.')
    return domain[-2:] == ['codwars', 'com']
