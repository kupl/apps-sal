def f(x):
    if(x%9==0):
        return 9
    else:
        return x%9
t=int(input())
for i in range(t):
    ran=input().split()
    ran=list(map(int,ran))
    a=ran[0]
    d=ran[1]
    l=ran[2]
    r=ran[3]
    s=0
    a=a+(l-1)*d
    for j in range(l,r+1):
        s+=f(a)
        a+=d
    print(s)

        
        
