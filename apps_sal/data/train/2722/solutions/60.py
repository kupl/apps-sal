def remove_url_anchor(url):
    if '#' not in url:
        return url
    else:
        get_index = list(url).index('#')
        return url[:get_index]
