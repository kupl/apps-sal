n = int(input())
s = list(map(int, input().split(' ')))
a = []
for i in range(max(s)):
    a.append([])
for i in range(len(s)):
    a[s[i] - 1].append(i)
a = list([x for x in a if x != []])
if len(a) > 1:
    for i in range(1, len(a)):
        if len(a[i]) > 1:
            s = a[i - 1][-1]
            if s > a[i][0] and s < a[i][-1]:
                for j in range(1, len(a[i])):
                    if s < a[i][j]:
                        a[i] = a[i][j:] + a[i][:j]
                        break
t = []
for i in a:
    t += i
c = 0
x = t[0] + 1
i = n - 1
while i > 0:
    if t[i] < t[i - 1]:
        k = t[i] - t[i - 1] + n
    else:
        k = t[i] - t[i - 1]
    c += k
    x -= c // n
    i -= 1
print(c + x)
