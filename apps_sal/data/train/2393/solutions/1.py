import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = [input()[:-1] + '1' for i in range(n)] + ['1' * (n + 1)]
    flag = True
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                continue
            if s[i + 1][j] == '1' or s[i][j + 1] == '1':
                continue
            flag = False
    if flag:
        print('YES')
    else:
        print('NO')
