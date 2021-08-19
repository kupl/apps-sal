n = 100000
prm = [True for i in range(n + 1)]
p = 2
while p * p <= n:
    if prm[p] == True:
        for i in range(p * 2, n + 1, p):
            prm[i] = False
    p += 1
c = []
for p in range(2, n):
    if prm[p]:
        c.append(p)
for _ in range(int(input())):
    k = int(input())
    s = 0
    for i in range(k):
        s = (s + c[c[i] - 1]) % (10 ** 9 + 7)
    print(s)
