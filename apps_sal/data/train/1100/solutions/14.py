# cook your dish here
t=int(input())
while t>0:
    p,q,r=list(map(int,input().split()))
    a,b,c=list(map(int,input().split()))
    x=a-p
    y=b-q
    z=c-r
    if x<0 or y<0 or z<0:
        print("-1")
    else:
        if x==0 and y==0 and z==0:
            print("0")
        elif x==0 and y==0:
            print(z)
        elif y==0 and z==0:
            print(x)
        elif x==0 and z==0:
            print(y)
        elif x==0:
            print(y+z)
        elif y==0:
            print(x+z)
        elif z==0:
            print(x+y)
        else:
            print(x+y+z)
        
    t-=1

