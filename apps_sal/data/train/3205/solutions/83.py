def is_divisible(n, x, y):
    ans = False
    if n % x == 0 and n % y == 0:
        ans = True
    return ans
