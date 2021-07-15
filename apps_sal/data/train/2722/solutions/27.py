def remove_url_anchor(url):
    if '#' in url: i = url.index('#')
    else: return url
    return url[:i]

