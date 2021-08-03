def remove_url_anchor(url):
    for x in url:
        y = len(url)
        if x == "#":
            y = url.index(x)
            break
    return url[:y]
