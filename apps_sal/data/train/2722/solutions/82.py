def remove_url_anchor(url):
    try:
        site, _ = url.split('#')
    except ValueError:
        return url
    else:
        return site
