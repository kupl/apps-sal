t = int(input())
for _ in range(t):
    v, w = list(map(int, input().split()))
    if w >= v:
        print(v + 1)
    else:
        print(w + 1)
