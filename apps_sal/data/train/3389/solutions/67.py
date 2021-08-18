def domain_name(url):
    print(url)
    if "www." in url:
        s = url.find("www.") + 4
    elif "//" in url:
        s = url.find("//") + 2
    else:
        s = 0

    e = url.find(".", s)

    return url[s:e]
