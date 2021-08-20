import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
t = int(input())
for _ in range(t):
    (r, c) = list(map(int, input().split()))
    s = [list(input()) for i in range(r)]
    cnt_a = 0
    flag_kado = False
    flag_hen = False
    flag_hen2 = False
    if s[0][0] == 'A' or s[0][c - 1] == 'A' or s[r - 1][0] == 'A' or (s[r - 1][c - 1] == 'A'):
        flag_kado = True
    for i in range(r):
        tmp = 0
        for j in range(c):
            if s[i][j] == 'A':
                if i == 0 or j == 0 or i == r - 1 or (j == c - 1):
                    flag_hen2 = True
                tmp += 1
        cnt_a += tmp
        if tmp == c and (i == 0 or i == r - 1):
            flag_hen = True
        elif tmp == c:
            flag_kado = True
    for i in range(c):
        tmp = 0
        for j in range(r):
            if s[j][i] == 'A':
                tmp += 1
        if tmp == r and (i == 0 or i == c - 1):
            flag_hen = True
        elif tmp == r:
            flag_kado = True
    if cnt_a == c * r:
        print(0)
    elif flag_hen:
        print(1)
    elif flag_kado:
        print(2)
    elif flag_hen2:
        print(3)
    elif cnt_a != 0:
        print(4)
    else:
        print('MORTAL')
