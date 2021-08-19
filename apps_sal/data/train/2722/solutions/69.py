def remove_url_anchor(url):
    count = 0
    if "#" in url:
        newUrl = url.replace(url[url.find("#"):], "")
        return newUrl
    else:
        return url
