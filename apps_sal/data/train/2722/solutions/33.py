def remove_url_anchor(url):
    ret = ""
    wh = len(url)
    for i in url:
        if i == "#":
            wh = url.index(i)
            break
    for i in range(0, wh):
        ret += url[i]
    return ret
