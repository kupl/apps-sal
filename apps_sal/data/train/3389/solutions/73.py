def domain_name(url):
    domain = ""
    if url.startswith("http"):
        url = url[url.find("//")+2:]
    if url.startswith("www."):
        domain = url[4:][:url[4:].find(".")] 
    else:
        domain = url[:url.find(".")]
    return domain

