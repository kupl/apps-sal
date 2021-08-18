n = int(input())
a = sorted(zip(map(int, input().split()), range(n)))
s = []

for i in range(n):
    if a[i]:
        s.append([])
        j = i
        while a[j]:
            s[-1].append(j + 1)
            a[j], j = None, a[j][1]

print(len(s))
for l in s:
    print(len(l), *l)
