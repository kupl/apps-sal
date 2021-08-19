def remove_url_anchor(url):
    anchor_pos = url.find('#')
    return url[0:anchor_pos if anchor_pos > 0 else len(url)]
