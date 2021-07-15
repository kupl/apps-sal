import re

def remove_url_anchor(url):
    regex = r'#\w+.+'
    subst = ''
    result = re.sub(regex, subst, url)
    return result
