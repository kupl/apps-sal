import math

def ModularInverse(a, b):
  #Use Euclidean algorithm, storing coefficients of each step
  coeffs = []
  while b > 0:
    coeffs.append(math.floor(a/b))
    a, b = b, a % b
  #Iterate back through all coefficients to construct coefficients for initial a and b
  c1 = 1
  c2 = 0
  for co in coeffs[::-1]:
    c1, c2 = c2, c1-co*c2
  return c2

def collatz_steps(n, steps):
  # Applying all U/D steps and simplifying results in...
  # (ax + b)/m is an integer, where 
  # a = 3 ^ (# of U in steps)
  # b = f(#steps-1) where
  #   f(-1) = 0
  #   f(i)=3f(i-1)+2^i when steps[i]==U
  #   f(i)=f(i-1)      when steps[i]==D
  # m = 2 ^ (#steps)
  a = 1
  b = 0
  m = 1
  for i in range(len(steps)):
    m = m * 2
    if steps[i] == 'U':
      a = a * 3
      b = 3*b + 2**i
  # Thus,
  # ax = -b mod m
  #  x = -ba^-1 mod m
  #  x = -ba^-1 + mC
  # Choose C such that n-m < x < n+m
  x = ((-b)*ModularInverse(m, a))%m + m*math.floor(n/m)
  if (x < n):
    x = x + m
  return x

