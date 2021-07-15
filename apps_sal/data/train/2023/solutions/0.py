from math import sqrt
n = int(input())
k = int(sqrt(n))
b = []
last = 0
while last < n:
    b.append([last + j for j in range(k)])
    last = b[-1][-1] + 1
k = len(b)
for i in range(k - 1, -1, -1):
    for j in b[i]:
        if j < n:
            print(1 + j, end=' ')
print()

