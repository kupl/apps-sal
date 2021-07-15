def remove_url_anchor(url):
    return url[:len(url) if url.find('#') == -1 else url.find('#')]
