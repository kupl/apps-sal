def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url
