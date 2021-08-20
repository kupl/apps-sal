y = [1, 5, 9, 15, 21]
for i in range(int(input())):
    s = 0
    x = input()
    for j in x:
        mn = 26
        for k in y:
            z = abs(k - (ord(j) - 96))
            if z < mn:
                mn = z
        s += mn
    print(s)
