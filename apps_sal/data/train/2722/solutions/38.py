def remove_url_anchor(url):
    hash = url.find('#')
    if hash == -1:
        return url
    else:
        new_url = url[0:hash]
        return new_url
