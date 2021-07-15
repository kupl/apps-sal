def filter_list(l):
  'return a new list with the strings filtered out'
  return [e for e in l if isinstance(e, int)]
