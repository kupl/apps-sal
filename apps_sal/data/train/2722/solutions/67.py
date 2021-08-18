def remove_url_anchor(url):
    a = 0
    for i in url:
        if i == '
        a = url.index(i)
    return url[:a] if a != 0 else url
