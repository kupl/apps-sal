# cook your dish here
for i in range(int(input())):

    s = input()
    z = s
    h = ""
    l = []
    k = 0
    while(len(z) != 0):
        if(k >= len(z)):
            break
        if(int(z[k]) < 6):
            f = z[k]
            z = z.replace(f, '')
            h = h + f
        else:

            f = z[k]
            h = h + f
            k += 1

    for i in range(len(h)):

        a = int(h[i])

        if(a >= 6):

            for j in range(len(h)):
                b = int(h[j])
                if(a == 6) and (b < 5):
                    continue
                if(j != i):

                    n = (a * 10) + b

                    if(n >= 65) and (n <= 90):

                        l.append(chr(n))

    l = set(l)
    l = list(l)
    l.sort()
    print("".join(l))
