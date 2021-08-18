n = int(input())
for i in range(n):
    w = input()
    l = len(w)
    s = 0
    a = 0
    for i in w:
        if i == 'a':
            a += 1
            s += 2**(l - a)
    print(s)
