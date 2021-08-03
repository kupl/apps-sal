n = int(input())
l = list(map(int, input().split()))
p = int(input())
s = sum(l[n - p:])
j = n - p
m = s
for i in range(p):
    t = s + l[i] - l[j]
    j += 1
    s = t
    if m < t:
        m = t
print(m)
