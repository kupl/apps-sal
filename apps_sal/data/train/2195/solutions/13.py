n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
d = 0
j = 0
m = 1
for i in range(1, len(a)):
    if a[i] == a[j]:
        m += 1
    else:
        if m > d:
            d = m
        m = 1
        j = i

if m > d:
    d = m

print(len(a) - d)
