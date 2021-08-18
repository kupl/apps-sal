S = str(input())
a = []
for i in S:
    a.append(i)
c = 0
for i in range(len(a) - 1, -1, -1):
    if a[i] == '1':
        for k in range(0, i + 1):
            if a[k] == '1':
                a[k] = '0'
            else:
                a[k] = '1'
        c = c + 1
print(c)
