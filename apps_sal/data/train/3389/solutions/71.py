def domain_name(url):
    domain = ''
    adding = False
    if 'www' in url:
        for char in url:
            if char == '.':
                adding = not adding
                if not adding: break
            if adding:
                domain += char
    elif url[6] == '/':
        for char in url:
            if char == '/':
                adding = True
            elif char == '.':
                adding = False
                break
            if adding:
                domain += char
    else:
        adding = True
        for char in url:
            if char == '.':
                adding = False
                break
            if adding:
                domain += char
            
    domain_arr = list(domain)
    if '/' in domain_arr: domain_arr.remove('/')
    if '/' in domain_arr: domain_arr.remove('/')
    if '.' in domain_arr: domain_arr.remove('.')
    print(url)
    return ''.join(domain_arr)
