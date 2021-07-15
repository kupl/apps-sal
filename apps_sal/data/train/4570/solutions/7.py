from functools import reduce

def clean_string(s):
  return reduce(lambda x, y: x[:-1] if y == '#' else x+y, s, "")
