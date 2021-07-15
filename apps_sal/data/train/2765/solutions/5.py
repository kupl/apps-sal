import re

def compare(a, b):
  [pa, pb] = [(x.count('#'), x.count('.'), len(re.findall(r"[\w']+", x)) - x.count('#') - x.count('.')) for x in [a, b]]
  return a if pa > pb else b
