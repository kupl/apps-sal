def chef(a, n):
    while n > 0:
        if a[-1] == "0":
            a = a[:-1]
            n -= 1
        else:
            a = str(int(a) - 1)
            n -= 1
    return a


b = list(map(str, input().split()))
print(chef(b[0], int(b[1])))
