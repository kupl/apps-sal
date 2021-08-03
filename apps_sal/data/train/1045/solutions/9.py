from sys import stdin, stdout
from collections import defaultdict
t = int(stdin.readline())
for _ in range(t):
    s = stdin.readline().strip()
    n = len(s)
    z = 0
    for i in range(n):
        if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            continue
        else:
            z += 2**(n - i - 1)
    print(z % 1000000007)
