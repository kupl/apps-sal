n, d = map(int, input().rstrip().split())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
i = n - 1
count = 0
while(i > 0):
    if l[i] - l[i - 1] <= d:
        i = i - 2
        count += 1
    else:
        i = i - 1
print(count)
