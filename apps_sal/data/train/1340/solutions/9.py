for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    p = 0
    for i in range(len(l)):
        if l[i] >= 0:
            p += 1
            ans += l[i]
    seq = []
    for i in range(len(l)):
        if i < p and l[i] < 0:
            seq.append(i + 1)
        elif i >= p and l[i] > 0:
            seq.append(i + 1)
    print(ans)
    print(len(seq), end=' ')
    for i in seq:
        print(i, end=' ')
    print()
