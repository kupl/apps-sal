from sys import stdin, stdout
a0 = 0
a1 = 1
(n, k) = stdin.readline().strip().split(' ')
(n, k) = (int(n), int(k))
arr = list(map(int, stdin.readline().strip().split(' ')))


def solve(n, k, arr):
    sol = []
    l = 0
    u = k
    while l != u:
        sol.append(arr[l:min(len(arr), u)])
        l = min(l + k, len(arr))
        u = min(u + k, len(arr))
    tiwari = []
    for i in range(k):
        titi = 0
        gao = 0
        for j in range(len(sol)):
            if len(sol[j]) > i:
                if sol[j][i] == 0:
                    titi += 1
                else:
                    gao += 1
        tiwari.append((titi, gao))
    minflip = (-1, -1)
    ans = 0
    ctr = 0
    for i in tiwari:
        if i[0] < i[1]:
            ans += i[0]
            ctr += (1 * a1 + a0 * a1) * a1
            if i[1] < minflip[0] or minflip[0] == -1:
                minflip = (i[1], i[0])
        else:
            ans += i[1]
            if i[0] < minflip[0] or minflip[0] == -1:
                minflip = (i[0], i[1])
    if ctr % 2 == 0:
        ans += minflip[0]
        ans -= minflip[1]
    stdout.write(str(ans) + '\n')


solve(n, k, arr)
