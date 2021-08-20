l = []
s = 0
for i in range(10 ** 5):
    s += i ** 2
    l.append(s)
for _ in range(int(input())):
    n = int(input())
    if n <= len(l):
        print(l[n - 1])
    else:
        for i in range(10 ** 4, n + 1):
            s += i ** 2
            l.append(s)
        print(s)
