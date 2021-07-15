def hex_to_dec(s):
  a=len(s)
  b={
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15
    }
  c={str(x):x for x in range(10)}
  for x in b:
    c[x]=b[x]
  d=0
  f=s[::-1]
  for x in range(len(s)-1,-1,-1):
    d += 16**x*c[f[x]]
  return d
