while(int(input()) != 0):
    l = list(map(int, input().split()))
    t = len(l)
    l1 = [0] * t
    for i in range(t):
        c = l[i]
        l1[c - 1] = i + 1
    if l == l1:
        print("ambiguous")
    else:
        print("not ambiguous")
