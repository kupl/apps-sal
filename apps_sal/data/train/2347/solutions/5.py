import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = input()
    poss = True
    sol = [2] * n
    ones = 0
    zeros = 0
    for i in range(n):
        if i < k:
            if s[i] == '1':
                sol[i] = 1
                ones += 1
            if s[i] == '0':
                sol[i] = 0
                zeros += 1
        else:
            if s[i] == '1':
                sol[i] = 1
                if sol[i - k] == 0:
                    poss = False
                if sol[i - k] == 2:
                    ones += 1
            if s[i] == '0':
                sol[i] = 0
                if sol[i - k] == 1:
                    poss = False
                if sol[i - k] == 2:
                    zeros += 1
            if s[i] == '?':
                if sol[i - k] == 1:
                    sol[i] = 1
                if sol[i - k] == 0:
                    sol[i] = 0
    if not poss or ones > k // 2 or zeros > k // 2:
        print('NO')
    else:
        print('YES')
