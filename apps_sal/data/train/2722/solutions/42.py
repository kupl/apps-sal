def remove_url_anchor(url):
    url_new = ''
    for i in url:
        if i == '#':
            return url_new
        url_new += i
    return url_new
