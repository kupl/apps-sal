import re
def domain_name(url):
    # checking for URL keyword
    if "www" in url:
        url = url.replace("www."  , "")
    regex1 = "\/\/[^.]+"
    regex2 = "[^.]+"
    if url.startswith("http"):
        domain = re.findall(regex1 , url)
    else:
        domain = re.findall(regex2 , url)


    if "//" in domain[0]:
        return domain[0][2:]
    else:
        return domain[0]
