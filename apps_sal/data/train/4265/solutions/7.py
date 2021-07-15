def tops(msg):
  i = 1
  j = 2
  res = []
  
  while i < len(msg):
    res.append(msg[i])
    i += 2*j+1
    j += 2
  
  return ''.join(res)[::-1]
