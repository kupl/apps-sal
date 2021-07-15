def domain_name(url):
    return url.split('//')[-1].split('.')[1] if 'www' in url else url.split('//')[-1].split('.')[0]
