def func(x, a):
    for amount in a:
        if amount >= x:
            return "YES"

    return "NO"


for _ in range(int(input())):
    a = input().split()
    n = int(a[0])
    x = int(a[1])
    print(func(x, map(int, input().split())))
