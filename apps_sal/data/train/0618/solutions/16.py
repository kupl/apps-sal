# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    li=[int(x) for x in input().split()]
    
    ''''en=li[-1]
    new=li[:len(li)-1]
    ma=new[0]+new[1]
    for i in range(1,len(new)-1):
        if(new[i]+new[i+1]>ma):
            ma=new[i]+new[i+1]
        
    #new.sort(reverse=True)
    print(en+ma)'''
    su=0
    st=0
    end=k-1
    for i in range(k):
        su+=li[i]
    res=su    
    for i in range(k,n+k):
        su+=(li[i%n]-li[(i-k)%n])
        if(su>res):
            res=su
    print(res)        
