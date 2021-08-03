def number_of_carries(a, b):
    ans, carrie = 0, 0
    while a > 0 or b > 0:
        carrie = (a % 10 + b % 10 + carrie) // 10
        ans += [0, 1][carrie > 0]
        a //= 10
        b //= 10
    return ans
