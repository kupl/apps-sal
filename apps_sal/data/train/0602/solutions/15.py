a = list(map(str, input().split()))
b = []
for j in a:
    b.append(len(j))
x = b.index(min(b))
y = a[x]
i = 0
while i < len(a):
    print(y, end=' ')
    print(a[i], end=' ')
    i += 1
print(y)
