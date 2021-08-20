def remove_url_anchor(url):
    url = url.split(sep='#')
    return url[0]
