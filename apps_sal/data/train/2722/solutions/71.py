def remove_url_anchor(url):
  index = url.find('#')
  if index == -1:
    return url
  else:
    return url[0:index]
