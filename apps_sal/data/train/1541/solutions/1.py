
eps=1e-8
t=int(input())
for ii in range(t):
    n=int(input())
    l=[int(i) for i in input().split() ]
    b=[int(i) for i in input().split() ]
    v=[int(i) for i in input().split() ]
    c=[int(i) for i in input().split() ]
    greatest_time=l[0]/v[0]
    for i in range(1,n):
        if v[i]>0:
            greatest_time=min(greatest_time,(l[i]-b[i])/v[i])
        elif v[i]<0:
            greatest_time=min(greatest_time,-b[i]/v[i])
    p = sum((b[i] - c[i]) ** 2 for i in range(n))
    q = sum(2 * (b[i] - c[i]) * v[i] for i in range(n))
    r = sum(vi ** 2 for vi in v)
    func = lambda t: p/t/t + q/t + r
    #ternary search
    
    def ternsearch():
    
        if b==c:
            return(0)
        
        lo,hi=0,greatest_time
        while hi-lo>eps:
                d=(hi-lo)/3
                m1=lo+d
                m2=m1+d
                if func(m1)<=func(m2):
                    hi=m2
                else:
                    lo=m1
                #print(hi,lo)
                #print(func(lo)**(0.5))
        return max(0,func(lo))**(0.5)
    ans=ternsearch()
    print('%.12f' % (ans,))
    
    

                
                

