n = int(input())
a = []
for i in range(0, n):
    no = int(input())
    a.append(no)
for i in range(0, n):
    c = 0
    s = 0
    while (a[i] != 0):
        c = a[i] % 10
        s = s * 10 + c
        a[i] = a[i] // 10
    print(s)
