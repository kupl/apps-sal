def reverse_list(l):
  ret = []
  for it in l:
      ret = [it] + ret
  return ret
