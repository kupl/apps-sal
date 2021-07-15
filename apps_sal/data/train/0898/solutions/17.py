for _ in range(int(input())):
    m,n=map(int,input().split())
    cn=0
    i=10
    while n>=i-1:
        cn+=1
        i=i*10    
    res=m*cn
    if cn==0:
        m=0
    print(res,m)            
