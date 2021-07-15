def nth_smallest(arr, pos):
    res = list(arr)
    i = 1
    while i < pos:
      m = min(res)
      for k, x in enumerate(res):
        if x == m:
            res[k] = 999999999
            break
      i = i + 1
    return min(res)
