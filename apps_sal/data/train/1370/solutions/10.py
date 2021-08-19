for _ in range(int(input())):
    (a, n) = map(int, input().split())
    a = set(str(a))
    if len(a) == 3:
        print(27)
    elif len(a) == 2:
        print(8)
    else:
        print(1)
