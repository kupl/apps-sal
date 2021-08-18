import sys
n, m, c = list(map(int, input().split()))

k = 1
li = []
query = m
rem = 0
if c <= query:
    query = c
    rem = m - query

for i in range(query):
    print(2, 1, n, k, k + 1 - 1)
    sys.stdout.flush()
    sum = int(input())
    li.append(str(sum / (n)))
    if k >= m:
        break
    k += 1
print(3)

for i in range(n):
    for j in range(query):
        print(li[j], end=' ')
    print(" ".join(["25"] * rem))
