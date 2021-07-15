def correct(string):
  return ''.join({'0':'O', '5':'S', '1':'I'}.get(c, c) for c in string)
