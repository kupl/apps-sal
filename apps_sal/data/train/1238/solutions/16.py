for i in range(int(input())):

    s = input()
    l = []
    for i in range(len(s)):

        a = int(s[i])

        if(a >= 6):

            for j in range(len(s)):
                b = int(s[j])
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
