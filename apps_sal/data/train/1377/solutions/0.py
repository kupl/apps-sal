for _ in range(int(input())):
    (x1, y1, x2, y2) = map(int, input().split())
    av1 = (x1 + y1) / 2
    av2 = (x2 + y2) / 2
    if av1 > av2:
        print(av1 - av2, ' DEGREE(S) ABOVE NORMAL')
    else:
        print(av2 - av1, ' DEGREE(S) BELOW NORMAL')
