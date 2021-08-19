t = int(input())
for x in range(t):
    (v, w) = input().split()
    v = int(v)
    w = int(w)
    if w > v:
        l = v + 1
    else:
        l = w + 1
    print(l)
