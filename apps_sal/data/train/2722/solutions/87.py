def remove_url_anchor(url):
    if '#' in url:
        slicer = url.index('#')
        return url[:slicer]
    else:
        return url
