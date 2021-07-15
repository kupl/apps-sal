n = int(input())
if n%2 == 0:
    print('NO')
else:
    a = [1]
    b = []
    i = 2
    c = 1
    while i<2*n:
        if c:
            b.append(i)
            b.append(i+1)
            c = 0
        else:
            a.append(i)
            a.append(i+1)
            c = 1
        i += 2
    b.append(2*n)
    ans = a + b
    print("YES")
    print(" ".join(str(x) for x in ans))
