t = int(input())
while t > 0:
    (v, w) = list(map(int, input().split()))
    if w < v:
        print(w + 1)
    else:
        print(v + 1)
    t = t - 1
