from re import search


def remove_url_anchor(url):
    pattern = r'(\A.+(?=#))'
    match = search(pattern, url)
    return match.group() if match else url
