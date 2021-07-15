import re

def remove_url_anchor(url):
    anchor = url.find('#')
    return url[:anchor] if anchor != -1 else url
