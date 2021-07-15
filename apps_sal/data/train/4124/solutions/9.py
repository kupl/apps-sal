def has_unique_chars(string):
  hash = [False] * 128
  for c in string:
      if hash[ord(c)]:
          return False
      hash[ord(c)] = True
  return True
