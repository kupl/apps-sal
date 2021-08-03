n = int(input())
a = []
for i in range(0, n):
    s = input()
    a.append(s)
c = 0
m = 0
for j in range(0, 7):
    for k in range(0, n):
        if a[k][j] == '1':
            c += 1
    m = max(c, m)
    c = 0
print(m)
