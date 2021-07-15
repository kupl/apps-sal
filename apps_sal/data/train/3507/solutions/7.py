def delete_nth(xs, max_count):
  ret=[]
  counts={x:0 for x in xs}
  for x in xs:
    counts[x]+=1
    if counts[x]<=max_count:
      ret.append(x)
  return ret
