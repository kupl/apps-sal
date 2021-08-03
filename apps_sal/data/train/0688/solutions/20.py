t = int(input())
s = []
for i in range(t):
    c = 0
    a = input()
    if a[0] != a[7]:
        c += 1
    for i in range(0, 6):
        if a[i] != a[i + 1]:
            c += 1
    s.append(c)
for i in s:
    if i <= 2:
        print("uniform")
    else:
        print("non-uniform")
