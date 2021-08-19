def remove_url_anchor(url):
    lst = url.split('#')
    url = str(lst[0])
    return url
