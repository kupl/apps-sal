def sum_div(n): return sum(d + n // d for d in range(2, int(n ** .5) + 1) if not n % d) + 1 - n**.5 / 1 * (not n**.5 % 1)
def amicable_numbers(x, y): return sum_div(x) == y and sum_div(y) == x
