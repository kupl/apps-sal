def solve(s):
    greater_letters = list(map(lambda x: 90 - ord(x), s))
    sum_value, tmp = 0, 0
    for value in greater_letters:
        sum_value += value*(1+tmp)
        tmp = (26*tmp + value) % 1000000007
    return sum_value % 1000000007
