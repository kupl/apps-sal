def remove_url_anchor(url):
    return url[0:url.find("#")] if "#" in url else url
