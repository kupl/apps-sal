n = int(input())
for i in range(0, n):
    o = input().rstrip().split(' ')
    q = int(o[1])
    x = int(o[0])
    t = list(str(bin(x)))
    del(t[0])
    del(t[0])
    while(len(t) < 30):
        t.insert(0, '0')
    # print(t)
    t.reverse()
    for j in range(0, q):
        o = int(input())
        if o == 1:
            p = int(input())
            if int(t[p - 1]) == 0:
                print("OFF")
            else:
                print("ON")
        elif o == 2:
            p = int(input())
            t[p - 1] = 1
        elif o == 3:
            p = int(input())
            t[p - 1] = 0
        else:
            E = input().rstrip().split(' ')
            A = int(E[0])
            B = int(E[1])
            temp = t[A - 1]
            t[A - 1] = t[B - 1]
            t[B - 1] = temp
