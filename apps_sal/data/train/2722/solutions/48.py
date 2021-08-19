def remove_url_anchor(url):
    anchor_pos = url.find('#')
    if anchor_pos > 0:
        return url[:anchor_pos]
    return url
