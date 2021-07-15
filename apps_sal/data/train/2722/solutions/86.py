from re import sub

def remove_url_anchor(url):
    return sub('#.+', '', url)
