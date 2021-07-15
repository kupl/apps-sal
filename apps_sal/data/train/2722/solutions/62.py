import re
def remove_url_anchor(url):
    return re.match(r'(.+)#', url)[1] if '#' in url else url
