def domain_name(url):
    print(url)
    split = url.split('.')
    if split[0] == 'www':
        return split[1]
    elif 'http://www' in split[0] or 'https://www' in split[0]:
        return split[1]
    elif 'http' in split[0] or 'https' in split[0]:
        split = split[0].split('//')
        return split[1]
    else:
        return split[0]
