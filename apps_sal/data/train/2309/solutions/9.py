for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    b.append(1)
    t = 10 ** 6
    used = [0] * (t + 1)
    used[1] = 1
    can_be = 2
    diffs = []
    for i in range(n):
        for j in range(i + 1, n):
            diffs.append(a[j] - a[i])
    for i in range(1, n):
        for j in diffs:
            used[min(b[i - 1] + j, t)] = 1
        while used[can_be]:
            can_be += 1
        b.append(can_be)
        used[can_be] = 1
    if len(b) == n:
        print('YES')
        for i in b:
            print(i, end=' ')
        print('')
    else:
        print('NO')
