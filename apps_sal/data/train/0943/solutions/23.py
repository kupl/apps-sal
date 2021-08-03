for t in range(int(input())):
    v, w = map(int, input().split())
    if v < w:
        print(1 + v)
    else:
        print(1 + w)
