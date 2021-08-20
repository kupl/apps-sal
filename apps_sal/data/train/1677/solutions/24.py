from itertools import accumulate
n = int(input())
a = tuple(map(int, input().split()))
b = tuple(accumulate(map(int, input().split())))
ssum = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            flag = a[i - 1]
        elif i < j:
            flag = a[i - 1] + a[j - 1] + (b[j - 2] - b[i - 1])
        elif j == 1:
            flag = a[i - 1] + a[j - 1] + (b[n - 1] - b[i - 1])
        else:
            flag = a[i - 1] + a[j - 1] + (b[n - 1] - b[i - 1]) + b[j - 2]
        ssum = max(ssum, flag)
print(ssum)
