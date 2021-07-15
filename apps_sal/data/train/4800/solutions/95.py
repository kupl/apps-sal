def hotpo(n, count=0):
  if n == 1:
    return count
  else:
    n = n/2 if is_even(n) else 3*n + 1
    count += 1
    return hotpo(n, count)

def is_even(n):
  return n % 2 == 0
