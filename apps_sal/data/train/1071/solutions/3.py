t = int(input())
while t:
    t -= 1
    b,k = list(map(int, input().split()))
    x = bin(b)[2:]
    n = len(x)
    for j in range(k):
        qu = int(input())
        if 1<=qu<=3:
            i = int(input())
            if qu==1:
                if i<=n:
                    r = n-i+1
                    if x[r-1]=='0':
                        print("OFF")
                    else:
                        print("ON")
                else:
                    print("OFF")
            elif qu==2:
                if i<=n:
                    r = n-i+1
                    x =x[0:r-1]+'1'+x[r:n]
                else:
                    x = '1' + (i-n-1)*'0' + x
                    n=i
            elif qu==3:
                if i<=n:
                    r = n-i+1
                    x =x[0:r-1]+'0'+x[r:n]
                    
                    
        else:
            p,q = list(map(int, input().split()))
            if p<=n and q<=n:
                r1 = n-p + 1
                r2 = n-q+1
                t1 = x[r1-1]
                t2 = x[r2-1]
                if x[r2-1]!=t1:
                    x = x[0:r2-1] + t1 + x[r2:n]
                if x[r1-1]!=t2:
                    x = x[0:r1-1]+t2+x[r1:n]
                
            elif p<=n:
                r1 = n-p+1
                p1 = x[r1-1]
                x =x[0:r1-1]+'0'+x[r1:n]
                if p1=='1':
                    x = '1'+(q-n-1)*'0' + x
                    n = q
            elif q<=n:
                r2 = n-q+1
                p2 = x[r2-1]
                x =x[0:r2-1]+'0'+x[r2:n]
                if p2=='1':
                    x = '1'+(p-n-1)*'0' + x
                    n=p
        

