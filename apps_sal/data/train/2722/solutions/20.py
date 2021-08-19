import re


def remove_url_anchor(url):
    pattern = re.compile(r'((http://?|https://?|http://www\.?|https://www\.?|www\.?|)+([a-zA-z0-9]+\.[a-zA-z0-9./-_]+))[^#]*')
    matches = pattern.finditer(url)
    for match in matches:
        return(match.group(1))
