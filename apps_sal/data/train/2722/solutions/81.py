def remove_url_anchor(url):
    if '#' in url:
        anchorPosition = url.find('#')
        return url[:anchorPosition]
    else:
        return url
