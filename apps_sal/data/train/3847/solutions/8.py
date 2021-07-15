def cycle(seq):
  
  seen = dict()
  
  for i, v in enumerate(seq):
    if v in seen:
      return [seen[v], i - seen[v]]
    else:
      seen[v] = i
  
  return []
