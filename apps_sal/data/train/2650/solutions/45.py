a = input().split()
c = int(a[0])
strlist = []
d = ''
for i in range(c):
    b = input().split()
    strlist.append(b[0])
strlist.sort()
for i in range(c):
    d += strlist[i]
print(d)
