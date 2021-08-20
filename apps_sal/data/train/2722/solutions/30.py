def remove_url_anchor(url):
    if '#' in url:
        anchorindex = url.index('#')
        return url[:anchorindex]
    else:
        return url
