t = int(input())
l = list()
for i in range(t):
    n = int(input()) / 10
    l.append(n)
for n in l:
    print(int(n * (n + 1) / 2.0 * 10))
