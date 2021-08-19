def remove_url_anchor(url):
    try:
        anchorIndex = url.index('#')
        return url[:anchorIndex]
    except:
        return url
