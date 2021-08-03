a = eval(input())
while(a):

    x = eval(input())
    b = list(map(int, input().split()))
    z = [0] * 100
    k = 1
    j = 0
    c = 0
    for i in b:

        if i == 0:

            z.insert(i, k)

        else:

            if z[z.index(i) + 1] == 0:

                z.insert(j, k)
            else:
                m = z.index(i)
                n = m + 1
                p = (len(z) - z.count(0)) - n
                c = c + min(n, p)

                z.insert(m + 1, k)

        k += 1
        j += 1
        m = 0
        n = 0
        p = 0

    print(c)

    a -= 1
