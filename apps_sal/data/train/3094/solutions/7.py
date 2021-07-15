def sum_array(arr):
  
  if arr is None or len(arr) < 2:
    return 0
  
  mi, ma, s = arr[0], arr[0], 0
  
  for x in arr:
    if x > ma:
      ma = x
    elif x < mi:
      mi = x
    
    s += x
  
  return s - mi - ma
