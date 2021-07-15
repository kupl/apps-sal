from itertools import groupby

def string_parse(string):
  return ''.join(f'{x*2}[{x*(c-2)}]' if c > 2 else x * c for x, c in [(x, len(list(gp))) for x, gp in groupby(string)]) if isinstance(string, str) else 'Please enter a valid string'
