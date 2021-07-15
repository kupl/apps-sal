def power_of_two(x):
  if x == 0: return False
  if x == 1: return True
  if x % 2 != 0: return False
  return power_of_two(x//2)
