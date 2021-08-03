l1 = input().split()
n = int(l1[0])
p = int(l1[1])
k = int(l1[2])
l = input().split()
A = {}

count = 0

e = []
for i in range(n):
    b = int(l[i])
    t = (b * b % p) * (b * b % p) - (k * b % p)
    t = t % p
    if t in A:
        A[t] += 1
    else:
        A[t] = 1

for x in A:
    count += int((A[x] * (A[x] - 1)) / 2)
print(count)
