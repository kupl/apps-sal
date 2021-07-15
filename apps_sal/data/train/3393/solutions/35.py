def divisors_list(num):
  divisors = []
  for i in range(1,int(num**0.5)+1):
    if num % i == 0:
      divisors += [i,num/i]
  return set(divisors)

def sum_squares(nums):
  return sum(num**2 for num in nums)

def isSquarable(num):
  return (num**0.5).is_integer()

def list_squared(m, n):
  res = []
  for i in range(m,n+1):
    elems_sum = sum_squares(divisors_list(i))
    if isSquarable(elems_sum):
      res.append([i, elems_sum])
  return res
