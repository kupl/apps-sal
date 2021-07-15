def remove_url_anchor(url):
    import re
    # TODO: complete
    new=re.split('#+',url)
    return new[0]
