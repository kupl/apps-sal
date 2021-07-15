def find_outlier(integers):
  even, odd = 0, 0
  for i in integers:
    if i % 2:
      even += 1
      last_even = i
    else:
      odd += 1
      last_odd = i
  return last_even if even == 1 else last_odd

