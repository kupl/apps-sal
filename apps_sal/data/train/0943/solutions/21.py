t = int(input())
for z in range(t):
    (v, w) = map(int, input().split())
    if w >= v:
        print(v + 1)
    else:
        print(w + 1)
