n = int(input())
a = []
for i in range(0, n):
    no = int(input())
    a.append(no)
for i in range(0, n):
    c = 0
    while (a[i] != 0):
        if (a[i] % 10 == 4):
            c += 1
        a[i] = a[i] // 10
    print(c)
