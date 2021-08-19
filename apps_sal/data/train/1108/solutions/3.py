# cook your dish here
n, m, k = map(int, input().split())
condit = 0
for _ in range(n):
    l = list(map(int, input().split()))
    a = 0
    for i in range(len(l) - 1):
        a += l[i]
    if a >= m and l[len(l) - 1] < 11:
        condit += 1

print(condit)
