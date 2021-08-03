import sys

n, r = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
s = sum(a)
n = 2**n
sys.stdout.write(str(s / n) + "\n")
for i in range(r):
    p, x = [int(x) for x in sys.stdin.readline().split()]
    s = s - a[p] + x
    a[p] = x
    sys.stdout.write(str(s / n) + "\n")
