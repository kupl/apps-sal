n, l, r, ql, qr = list(map(int, input().split()))
w = list(map(int, input().split()))
sum = 0
sums = []
for i in range(n):
    sum += w[i]
    sums.append(sum)

min = r * sum + qr * (n - 1)
for i in range(n):
    ss = l * sums[i] + r * (sum - sums[i])
    if i + 1 > n - i - 1 and i - n + i + 1 > 0:
        ss += ql * (i - n + i + 1)
    elif i + 1 < n - i - 1 and n - i - 2 - i > 1:
        ss += qr * (n - i - 2 - i - 1)
    if ss < min:
        min = ss
print(min)


