from sys import stdin, stdout
n = int(stdin.readline())
while n:
    n -= 1
    k, l, e = map(int, stdin.readline().strip().split(' '))
    a = map(int, stdin.readline().strip().split(' '))
    x = float(l) / float(e + sum(a))
    if x - int(x):
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
