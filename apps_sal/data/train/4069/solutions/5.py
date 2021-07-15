memoize = {}
def nth_fib(n):
  if n == 1: 
     return 0 
  if n == 2: 
     return 1 
  if n not in memoize: 
     memoize[n] = nth_fib(n-1) + nth_fib(n-2) 
  return memoize[n]


