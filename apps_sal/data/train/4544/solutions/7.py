def aux(x):
    s = 0
    i = 2
    while x > 1:
        while x % i == 0:
            s += i
            x /= i
        i += 1
    return s
def factor_sum(num):
    l = None
    while l != num:
        l = num
        num = aux(num)
    return l
