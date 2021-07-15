def spinning_rings(innermax,outermax):
    if innermax>outermax:
        a = innermax
        b = 1
        c = 1
        if a>outermax and outermax*2<innermax:
            c+=(a-outermax)
            b+=(a-outermax)%(outermax+1)
            if b>outermax:
                b=0
            a=outermax

        while a != b:
            if a>outermax and c!=b:  # check if a> outermax than a become in outer max range.
                temp=c
                c+=(a-outermax)
                b=(b+(c-temp))%(outermax+1)
                a=outermax
            if (a%2)==(b%2):
                return c+(a-b)//2
            elif a<b:
                c+=a+1
                b+=(a+1)%(outermax+1)
                a=innermax
            elif a>b:
                c+=(outermax-b+1)
                a=a-(outermax-b+1)
                b=0
            if a == 0:
                a = innermax
            else:
                a -= 1
            if b == outermax:
                b = 0
            else:
                b += 1
            c += 1
        else:
            return c

    else:
        a = innermax
        b = 1
        c = 1
        if a % 2 != 0:
            return a // 2 + 1
        while a != b:

            if a % 2 == 1 and b % 2 == 1:
                return c + (a // 2 + 1)
            elif a > b and a % 2 == 0 and b % 2 == 0:
                return c + (a - b) // 2
            else:

                c = c + a
                b = b + a
                a = 0
            if b > innermax:
                a = abs((a - (outermax - b)) % (innermax + 1))
                c += (outermax - b)
                b = outermax
            if a == 0:
                a = innermax
            else:
                a -= 1
            if b == outermax:
                b = 0
            else:
                b += 1
            c += 1
        else:
            return c
