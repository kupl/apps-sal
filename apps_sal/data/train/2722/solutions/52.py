def remove_url_anchor(url):
    new = url.find('#')
    if new > 0:
        return url[0:new]
    else:
        return url
