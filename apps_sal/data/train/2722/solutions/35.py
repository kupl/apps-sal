def remove_url_anchor(url):
    index = url.find('#')
    return url[:index if index > 0 else len(url)]
