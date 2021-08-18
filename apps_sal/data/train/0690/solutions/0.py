n, k, m = map(int, input().split())
ar = list(map(int, input().split()))
fsum = [ar[0]]
for i in range(1, n):
    fsum.append(fsum[i - 1] + ar[i])
i = k
c = 0
while i <= n:
    if i == k:
        s = fsum[i - 1]
    else:
        s = fsum[i - 1] - fsum[i - k - 1]
    if s == 0:
        c = -1
        break
    if s < m:
        c += 1
        if i < n:
            for j in range(i, i - k - 1, -1):
                if ar[j - 1] > 0:
                    j += k - 1
                    i = j
                    break
        if i < n:
            for j in range(i, i - k - 1, -1):
                if ar[j - 1] > 0:
                    j += k - 1
                    i = j
                    break
    i += 1
i = k
while i <= n:
    if i == k:
        s = fsum[i - 1]
    else:
        s = fsum[i - 1] - fsum[i - k - 1]
    if s == 0:
        c = -1
        break
    i += 1
print(c)
