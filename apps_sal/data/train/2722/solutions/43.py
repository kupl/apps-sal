def remove_url_anchor(url):
    fixed_url = url.split('#')
    return fixed_url[0]
