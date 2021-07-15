def domain_name(url):
    print(url)
    url = url.replace("http://","")
    url = url.replace("https://","")
    url = url.replace("www.","")
    end = url.find(".")
    return url[0:end]
