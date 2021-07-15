def is_onion_array(a):
  i = 0; j = -1
  while i != len(a)//2:
    if a[i] + a[j] > 10:
      return False
    i += 1
    j -= 1
  return True
