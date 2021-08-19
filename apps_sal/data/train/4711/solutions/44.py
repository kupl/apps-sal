from math import factorial


def zeros(n):
    if n == 0:
        return 0
    cnt = 0
    div_num = 5
    while n / div_num >= 1:
        cnt += int(n / div_num)
        div_num *= 5
    return cnt
