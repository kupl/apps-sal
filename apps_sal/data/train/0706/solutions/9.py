t = int(input())
for i in range(t):
    (s, c) = (0, 0)
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if max(l) > k:
        print('-1')
    else:
        for i in range(len(l)):
            s += l[i]
            if s > k:
                c += 1
                s = l[i]
        if s > 0:
            c += 1
        print(c)
