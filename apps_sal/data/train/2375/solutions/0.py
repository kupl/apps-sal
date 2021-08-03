from operator import itemgetter
import sys
input = sys.stdin.readline

MAX_A = 200
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ruiseki = [[0] * MAX_A for i in range(n + 1)]
    for i in range(n):
        for j in range(MAX_A):
            ruiseki[i + 1][j] = ruiseki[i][j]
            if a[i] - 1 == j:
                ruiseki[i + 1][j] += 1

    ans = 0
    for num in set(a):
        l = 0
        r = n - 1
        cnt = 0
        while True:
            while True:
                if a[l] != num:
                    l += 1
                else:
                    break
            while True:
                if a[r] != num:
                    r -= 1
                else:
                    break
            if l == r:
                ans = max(ans, cnt + 1)
                break
            elif l > r:
                break
            cnt += 1
            tmp_max = 0
            for j in range(MAX_A):
                tmp_max = max(tmp_max, ruiseki[r][j] - ruiseki[l + 1][j])
            ans = max(ans, cnt * 2 + tmp_max)
            l += 1
            r -= 1
    print(ans)
