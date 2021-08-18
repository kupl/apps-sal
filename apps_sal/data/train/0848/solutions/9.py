from sys import stdin, stdout

s = ""
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = 0
    for i in range(-1, n - 2):
        x = a[i] + a[i + 1] + a[i + 2]
        if m < x:
            m = x
    x = a[n - 2] + a[n - 1] + a[0]
    if m < x:
        m = x
    s += str(m) + "\n"

stdout.write(s)
