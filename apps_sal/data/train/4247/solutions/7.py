def odd(s):
  n, o, d, trying = 0, 0, 0, True
  while trying:
    try:
      o += s[o:].index('o') + 1
      d = max(o, d)
      d += s[d:].index('d') + 1
      d += s[d:].index('d') + 1
      n += 1
    except:
      trying = False
  return n

