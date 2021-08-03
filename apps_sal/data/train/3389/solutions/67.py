def domain_name(url):
    print(url)
    # finds start of url
    if "www." in url:
        s = url.find("www.") + 4
    elif "//" in url:
        s = url.find("//") + 2
    else:
        s = 0

    # finds end of url
    e = url.find(".", s)

    return url[s:e]
