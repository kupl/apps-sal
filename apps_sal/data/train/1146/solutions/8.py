(n, d) = map(int, input().split())
a = []
for i in range(n):
    num = int(input())
    a.append(num)
a.sort()
i = 0
count = 0
while i < n - 1:
    if a[i + 1] - a[i] <= d:
        count = count + 1
        i = i + 2
    else:
        i = i + 1
print(count)
