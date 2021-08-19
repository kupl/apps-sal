def remove_url_anchor(url):
    new_url = ''
    for i in url:
        if i == "#":
            return new_url
        new_url += i
    return url
