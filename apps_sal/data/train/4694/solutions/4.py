from math import factorial
(result, x, y) = ([0], 0, 1)
for _ in range(20):
    result.append(result[-1] + factorial(x))
    (x, y) = (y, x + y)
sum_fib = result.__getitem__
