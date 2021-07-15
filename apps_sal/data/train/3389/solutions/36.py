def domain_name(url):
    if "w" * 3 in url:
        new_url = url[(url.index(".") + 1):]
        return new_url[: new_url.index(".")]

    elif "/" * 2 in url:
        return url[(url.index("/") + 2):url.index(".")]

    else:
        return url[:url.index(".")]
