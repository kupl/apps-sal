def domain_name(url):
    url = url.replace('http://www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.replace('www.', '')
    a = ''
    for i in url:
        if i != '.':
            a = a + i
        else:
            return a
