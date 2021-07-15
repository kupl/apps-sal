from sys import stdin, stdout
from random import randrange

s = stdin.readline().strip()
n = len(s)
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for z in range(j + 1, n):
            if s[i] == 'Q' and s[j] == 'A' and s[z] == 'Q':
                ans += 1

stdout.write(str(ans))
