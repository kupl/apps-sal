def prime_string(s):
  return True if (s+s).find(s, 1, -1) == -1 else False
