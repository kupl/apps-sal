def nth_fib(n):
  return 0 if n==1 else 1 if n in [2,3] else (nth_fib(n-2)+nth_fib(n-1))
