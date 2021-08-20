def remove_url_anchor(url):
    a = []
    for i in url:
        if i == '#':
            break
        a.append(i)
    return ''.join(a)
