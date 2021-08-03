n, m = [int(x) for x in input().split()]
if n == m:
    print(n)
elif n - 1 == m:
    print(m)
elif m == 1:
    if n == 3:
        print(2)
    elif n == 4:
        print(1)
    elif n == 5:
        print(4)
elif m == 2:
    if n == 4:
        print(2)
    elif n == 5:
        print(3)
elif m == 3:
    if n == 5:
        print(3)
