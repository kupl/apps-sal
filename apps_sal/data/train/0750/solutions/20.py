while int(input()):
    l = list(map(int, input().split()))
    h = len(l)
    l1 = [0] * h
    for i in range(h):
        c = l[i]
        l1[c - 1] = i + 1
    if l == l1:
        print('ambiguous')
    else:
        print('not ambiguous')
