def list_depth(l):
  return max(1 + list_depth(x) if type(x) is list else 1 for x in l) if l else 1
