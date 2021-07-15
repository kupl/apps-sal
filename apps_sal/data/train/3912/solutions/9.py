def arr2bin(arr):
  try:
    return bin(sum(int(x) if not isinstance(x, bool) else None for x in arr))[2:]
  except:
    return False
