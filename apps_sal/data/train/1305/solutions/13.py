for ts in range(int(input())):
    N = int(input())
    l = []
    f = 1
    while not l or len(l) < len(l[0]):
        l.append(list(map(int, input().split())))
    p = sum(l, [])
    k = [i for i in range(len(p)) if p[i] == 1]
    for j in range(len(k) - 1):
        if k[j + 1] - k[j] == 1:
            f = 0
            break
    if f == 0:
        print('UNSAFE')
    else:
        print('SAFE')
