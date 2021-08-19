try:
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        p = []
        for i in range(n):
            for j in range(i + 1, n):
                p.append(l[i] + l[j])
        m = p.count(max(p)) / len(p)
        print('%.8f' % m)
except:
    pass
