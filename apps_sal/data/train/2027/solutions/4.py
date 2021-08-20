k = input()
s = []
a = []
b = []
for i in range(len(k)):
    if k[i] == 'l':
        a.append(i + 1)
    else:
        b.append(i + 1)
a.reverse()
for i in b:
    print(i)
for i in a:
    print(i)
