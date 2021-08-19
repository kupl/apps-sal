import sys
input = sys.stdin.readline
x = [98, 57, 31, 45, 46]
t = int(input())
for _ in range(t):
    p = list(input().strip())
    ans = ''
    for i in range(len(p)):
        ans += chr((int(ord(p[i])) - 65 + x[i]) % 26 + 65)
    print(ans)
