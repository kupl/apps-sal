t = int(input())
for _ in range(t):
    a = input()
    c = 0
    m = 0
    for i in range(len(a)):
        if c == 6:
            c = 0
            continue
        if a[i] == 'M':
            m += 3
            c += 1
            continue
        if a[i] == 'L':
            m += 4
            c += 1
            continue
    print(m)
