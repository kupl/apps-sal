
def triangle(a):

    q = len(a)
    if q == 1:
        return(a)

    b = 1
    g = 2
    r = 3

    a = a.replace('B', '1')
    a = a.replace('G', '2')
    a = a.replace('R', '3')

    v = int(a)

    kj = 1
    me = 0
    while me == 0:
        if (q > 3**kj):
            kj = kj+1
        else:
            me = 1

    g = 3**(kj-1)


    count = 0
    while q != 1:
        if (q > g):
            for w1 in range (0,(q-g)):
                q1 = str(v)
                e = (3 - ((( int(q1[w1]))+ int(q1[w1+g]))%3))
                count = count + e*(10**(q-w1-g-1))
            print((g,q))
            q = q-g           
            if (q > g):
                g = g
            else:
                g = int(g/3)
            print((g,q))
            v = count
            print (count)
        else:
            for i in range (1,q):
                e = 3 - (((((v//(10**(q-i)))-(10*(v//(10**(q-i+1)))))+(v//(10**(q-i-1)))-(10*(v//(10**(q-i)))))%3))
                count = count + e*(10**(q-i-1))
            q = q-1
            v = count
            print (count)
        if q == 1:
            if count == 1:
                return ("B")
            else:
                if count == 2:
                    return ("G")
                else:
                    return ("R")
        count = 0

