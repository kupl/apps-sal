def domain_name(url):
    d = url.split('//')
    try:
        f = d[1].split('.')
    except IndexError:
        f = d[0].split('.')
    return f[0] if f[0] != 'www' else f[1]
