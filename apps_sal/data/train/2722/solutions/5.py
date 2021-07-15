def remove_url_anchor(url):
  try:
    return url[:url.index('#')]
  except:
    return url
