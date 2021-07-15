import re

def isDigit(string):
  return bool(re.search(r'^-?[\d\.]+$', string))
