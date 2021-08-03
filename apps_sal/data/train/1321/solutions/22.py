from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(((n - 1) * (n) * ((2 * (n - 1)) + 1)) // 6)
