from sys import stdin as s
t = int(s.readline())
while t:
    t -= 1
    n = int(s.readline())
    for _ in range(n):
        a = s.readline()
    print(n * (n + 1) // 2)
