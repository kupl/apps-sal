t = int(input())
for cases in range(t):
    a, b, c = list(map(int, input().split()))
    if c > b and c > a:
        if b > a:
            print(b)
        else:
            print(a)
    elif b > c and b > a:
        if c > a:
            print(c)
        else:
            print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)
    print()
