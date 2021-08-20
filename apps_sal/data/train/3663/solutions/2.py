def four_piles(n, y):
    x = y * n / (1 + 2 * y + y ** 2)
    ans = [x + y, x - y, x * y, x / y]
    return ans if all((not z % 1 and z for z in ans)) else []
