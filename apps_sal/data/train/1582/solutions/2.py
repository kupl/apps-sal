def chef(n, a):
    c = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            c += 1
    return c


c = int(input())
b = input()
print(chef(c, b))
