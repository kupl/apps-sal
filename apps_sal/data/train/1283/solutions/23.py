# cook your dish here
import math
def prime(n):
    c=0
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:    
        for i in range(2,math.floor(math.sqrt(n))+1):
            if(n%i==0):
                c=1
                break
        if(c==0):
            return 1
        else:
            return 0
for i in range(int(input())):
    k=int(input())
    e=0
    for i in range(1,k+1):
        for j in range(i,k+1):
            if(i+j==k):
                c,d=0,0
                for m in range(1,i+1):
                    for n in range(m,i+1):
                        if(m*n==i and m!=n):
                            if(prime(m) and prime(n)):
                                c=1
                                break
                    if(c==1):
                        break
                for o in range(1,j+1):
                    for p in range(o,j+1):
                        if(o*p==j and o!=p):
                            if(prime(o) and prime(p)):
                                d=1
                                break
                    if(d==1):
                        break
                if(c and d):
                    e=1
                    break
        if(e==1):
            break
    if(e==1):
        print("YES")
    else:
        print("NO")
