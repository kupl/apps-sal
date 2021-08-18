import math
try:

    t = int(input())

    while(t > 0):
        n = int(input())
        c = 0
        '''while(n>=1):
            if(n%2==1):
                c=c+1
            n=n//2'''
        m = n
        s = 0
        if(math.log2(n) - int(math.log2(n)) == 0):
            print(0)
        else:
            while(n >= 2):
                if(bool(math.log2(n))):
                    c = c + 1
                r = 2**(int(math.log2(n)))
                s = s + r
                n = n - r

                if(s == m):
                    c = c - 1
            print(c)
        t = t - 1
except:
    pass
