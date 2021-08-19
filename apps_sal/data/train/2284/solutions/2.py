import sys
input = sys.stdin.readline
s = input()
q = int(input())
query = [tuple(map(int, input().split())) for i in range(q)]
char = [[0] * 26 for i in range(len(s) + 1)]
for i in range(len(s)):
    si = ord(s[i]) - 97
    for j in range(26):
        if j == si:
            char[i + 1][j] = char[i][j] + 1
        else:
            char[i + 1][j] = char[i][j]
for (l, r) in query:
    count = 0
    for i in range(26):
        if char[r][i] - char[l - 1][i] != 0:
            count += 1
    if count == 1:
        if r == l:
            print('Yes')
        else:
            print('No')
    elif count == 2:
        if s[r - 1] == s[l - 1]:
            print('No')
        else:
            print('Yes')
    else:
        print('Yes')
