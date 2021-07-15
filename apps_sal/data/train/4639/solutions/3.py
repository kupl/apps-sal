def power_of_two(x):
  # your code here
  return x > 0 and (x & (x-1)) == 0
