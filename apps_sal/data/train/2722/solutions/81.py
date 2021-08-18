def remove_url_anchor(url):
    if '
        anchorPosition = url.find('
        return url[:anchorPosition]
    else:
        return url
