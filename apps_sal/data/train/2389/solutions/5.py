from sys import stdin, stdout
input = stdin.readline
for _ in range(int(input())):
    x = 10**5
    n, k = list(map(int, input().split()))
    s = input()
    a = 10**9
    ans = [[0] * n for i in range(3)]
    curr = ['R', 'G', 'B']
    for l in range(3):
        z = l
        for j in range(n):
            if s[j] != curr[z]:
                ans[l][j] = 1
            z += 1
            z %= 3
    for i in range(3):
        ans[i] = [0] + ans[i]
    for l in range(3):
        z = l
        for j in range(1, n + 1):
            ans[l][j] += ans[l][j - 1]
    for l in range(3):
        for j in range(1, n - k + 2):
            a = min(a, ans[l][j + k - 1] - ans[l][j - 1])
    print(a)
