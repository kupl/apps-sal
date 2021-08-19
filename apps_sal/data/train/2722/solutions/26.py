def remove_url_anchor(url):
    import re
    new = re.split('#+', url)
    return new[0]
