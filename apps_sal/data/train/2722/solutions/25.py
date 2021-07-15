def remove_url_anchor(url):
    try:
        ret_url, non_url = url.split('#', 1)
        return ret_url
    except:
        return url

