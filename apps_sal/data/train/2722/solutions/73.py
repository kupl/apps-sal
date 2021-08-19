def remove_url_anchor(url):
    new_url = ""
    if "#" in url:
        i = url.index("#")
        new_url = url[0: i]
    else:
        new_url = url
    return new_url
