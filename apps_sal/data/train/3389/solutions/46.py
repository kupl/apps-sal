def domain_name(url):
    if "www." in url:
        startpos = url.find("www.") + 4
    elif "://" in url:
        startpos = url.find("://") + 3
    else:
        startpos = 0
    endpos = url.find(".", startpos)
    return(url[startpos:endpos])
