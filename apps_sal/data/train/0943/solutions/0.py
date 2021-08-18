t = int(input())
for i in range(t):
    v, w = list(map(int, input().strip().split(" ")))
    if v == w:
        print(v + 1)
    elif v < w:
        print(v + 1)
    else:
        print(w + 1)
        ct = 0
