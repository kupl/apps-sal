t = int(input())
i = 0
while i < t:
    i = i + 1
    (a, b, c) = list(map(int, input().split()))
    if a > b and a > c:
        if b > c:
            print(b)
        else:
            print(c)
    elif b > c and b > a:
        if a > c:
            print(a)
        else:
            print(c)
    elif a > b:
        print(a)
    else:
        print(b)
