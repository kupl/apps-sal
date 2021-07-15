def majority(arr):
  dic = {}
  n = 0
  c = 0
  for x in arr:
      if not x in dic:
          dic[x] = 1
      else:
          dic[x] += 1
  for x in dic:
      n = max(n,dic[x])
  for x in dic: 
      if dic[x] == n: 
          r = x
          c += 1
  if c==1: 
      return r
  else:
      return None
