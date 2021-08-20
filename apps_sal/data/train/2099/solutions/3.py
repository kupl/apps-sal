(n, k) = list(map(int, input().split()))
a = []
for i in range(1, n - k + 1):
    a.append(i)
(i, j) = (n, n - k + 1)
for t in range(n - len(a)):
    if t % 2 == 0:
        a.append(i)
        i -= 1
    else:
        a.append(j)
        j += 1
print(' '.join(map(str, a)))
