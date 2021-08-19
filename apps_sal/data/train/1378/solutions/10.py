(a, n, k) = map(int, input().split())
l = [0 for i in range(k)]
j = 0
while j < k:
    l[j] = a % (n + 1)
    a = a // (n + 1)
    j += 1
for j in l:
    print(j, end=' ')
