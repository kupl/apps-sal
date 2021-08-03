
t = input()
for i in range(int(t)):
    s = input()
    l, r, f = 0, 0, 0
    for j in s:
        if(j == 'W'):
            f = 1
            continue
        if(f != 1):
            l += 1
        else:
            r += 1
    if(l == r):
        print("Chef")
    else:
        print("Aleksa")
