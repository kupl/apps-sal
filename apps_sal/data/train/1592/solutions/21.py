for _ in range(int(input())):
    n = int(input())
    chef, f = 0, []
    for i in range(n):
        l = list(map(int, input().split()))
        b = l[0]
        if b & 1:
            f.append(l[(b // 2) + 1])
        for i in range(1, (b // 2) + 1):
            chef += l[i]
    print(chef + sum((sorted(f, reverse=True))[::2]))
