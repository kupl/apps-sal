t = int(input())
for h in range(t):
    a = input()
    b = input()
    aset = set(a)

    c = 0
    for i in aset:
        if i in b:
            c = c + min(a.count(i), b.count(i))
    print(c)
