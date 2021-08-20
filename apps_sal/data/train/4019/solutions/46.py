def max_multiple(a, b):
    res = 0
    for i in range(b + 1):
        if i % a == 0:
            if i > res:
                res = i
    return res


print(max_multiple(10, 50))
