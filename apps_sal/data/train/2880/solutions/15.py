def seven(m, k = 0):
  s = str(m)
  l = len(s)
  k += 1
  if l >= 3:
    m = int( s[:l-1] ) - 2 * int( s[-1] )
  else: return (m, k-1)
  return seven(m, k)
