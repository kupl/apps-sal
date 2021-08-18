def remove_url_anchor(url):
    if "
        anchorindex = url.index("
        return url[:anchorindex]
    else:
        return url
