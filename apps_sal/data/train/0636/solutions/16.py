x = list(map(int,input().split()))
n = x[0]
t = x[1]
a = x[2:n+2]
a.sort()

sums = [0] * t
count = 0
for i in range(n):
    for j in range(i+1,n):
        add = a[i] + a[j]
        if add < t:
            count += sums[t-add]
    for k in range(i):
        add = a[i] + a[k]
        if add<t:
            sums[add] += 1

print(count)
