def divisors(n):
  dividend=[i for i in range(n) if n%(i+1)==0]
  return len(dividend)
