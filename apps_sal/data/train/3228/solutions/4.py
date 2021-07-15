def word_pattern(pattern, s):
  s = s.split()
  return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)) and len(s) == len(pattern)
