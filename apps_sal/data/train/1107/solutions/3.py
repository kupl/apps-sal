def len(n):
    x=0
    while n>0:
        x+=1
        n=n//10
    return x
e=10**9+7
t=int(input())
#l=[0]
#for i in range(1,10**7):
    #l.append((l[-1]+i*len(i))%e)

f=[0]
a=9
b=1
for i in range(10):
    x=(2*b+a-1)%e
    x=(x*a)%e
    y=pow(2,e-2,e)
    x=(x*y)%e
    x=(x*(i+1))%e
    x=(x+f[-1])%e
    b*=10
    a*=10
    
    f.append(x)
#print(f)
def ans(n):
    if n==0:
        return 0
    x=len(n)
    y = f[x-1]
    a=pow(10,x-1,e)
    b=((n+a)*(n-a+1))%e
    b =(b*pow(2,e-2,e))%e
    b=(b*x)%e
    #print(y,b,n)
    return (b+y)%e
    
    
for _ in range(t):
    a,b=map(int,input().split())
    #print(l[b]-l[a-1])
    b = ans(b)
    a=ans(a-1)
    print((b-a)%e)
    

