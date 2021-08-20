(x, y) = list(map(str, input().split(' ')))
l = list(x)
y = int(y)
i = 0
while i < int(y):
    if l[i] != '9':
        l[i] = '9'
    else:
        y += 1
    i += 1
print(''.join(l))
