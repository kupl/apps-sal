def remove_url_anchor(url):
    return url[:list(url).index('#')] if '#' in url else url
