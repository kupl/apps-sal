def remove_url_anchor(url):
    if '#' in url:
        return ''.join(list(url)[:list(url).index('#')])
    else:
        return url
  # TODO: complete
