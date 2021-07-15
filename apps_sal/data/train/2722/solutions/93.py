def remove_url_anchor(url):
    try:
        a = url.index("#")
        return url[:a]
    except Exception:
        pass
    return url
