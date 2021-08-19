def remove_url_anchor(url):
    return url if url.count('#') == 0 else url[:url.index('#')]
