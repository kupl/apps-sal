def flatten(lst):
    #your code here\
    res = []
    for i in lst:
      if isinstance(i, list):
        res.extend(i)
      else:
        res.append(i)
    return res
