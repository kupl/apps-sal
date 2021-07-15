def domain_name(url):
    url = url.replace("www.","").split("/")
    for i in url:
        if '.' in i:
            url = i
            break
    domain,mid,tail = url.partition(".")
    return domain
