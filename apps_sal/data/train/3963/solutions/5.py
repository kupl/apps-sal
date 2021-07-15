#sum_div = lambda n: sum(d for d in range(1, n) if not n%d)
sum_div = lambda n: sum(d + n // d for d in range(2, int(n ** .5) + 1) if not n%d) + 1 - n**.5/1 * (not n**.5%1)
amicable_numbers = lambda x, y: sum_div(x) == y and sum_div(y) == x
