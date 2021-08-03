def mult(s):
    re = s[0]
    for i in s[1:]:
        re = re * i
    return re


def max_product(lst, n):
    return mult(sorted(lst, reverse=True)[:n])
