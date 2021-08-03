from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    c = 0
    n = int(input())
    s = input()
    for i in range(1, n):
        if s[i - 1] == s[i]:
            c += 1
    print(c)
