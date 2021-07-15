from itertools import groupby

def is_alt(s):
  return all(len(list(gp)) == 1 for _, gp in groupby(s, key = lambda x: x in 'aeiou'))
