def domain_name(url):
    print(url)
    first = ""
    second = ""

    if "www" in url:

        first = url.split("www.")[1]
        second = first.split(".")[0]

    elif "http" in url:
        first = url.split("://")[1]

        second = first.split(".")[0]

    else:
        second = url.split(".")[0]

    return second
