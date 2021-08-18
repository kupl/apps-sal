while int(input()) != 0:
    l = list(map(int, input().split()))
    ln = len(l)
    ll = [0] * ln
    for i in range(ln):
        k = l[i]
        ll[k - 1] = i + 1
    if l == ll:
        print("ambiguous")
    else:
        print("not ambiguous")
