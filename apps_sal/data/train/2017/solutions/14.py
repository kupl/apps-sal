n = input()
n = int(n)
a = [int(i) for i in input().split()]
d = []
l = []
n = 2 * n
d = {i: -1 for i in a}
point = 0
count = 0
for i in range(0, n):
    l.append(a[i])
    if d[a[i]] == -1:
        d[a[i]] = 0
    elif d[a[i]] == 0:
        d[a[i]] = 1
        j = l.index(a[i])
        l.pop()
        l.insert(j + 1, a[i])
        count = count + (i - j - 1)
        if j == point:
            point = point + 2
print(count)
