def power_of_two(x):
  # your code here
  if str(bin(x))[2:].count("1")==1:
      return True
  else:
      return False
