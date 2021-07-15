def prime(n):  
    l1 =[True]*(n + 1) 
    i=2
    while i*i<=n:
        if l1[i]==True: 
            a=i*2
            while a<=n: 
                l1[a]=False
                a=a+i 
        i=i+1    
    s1=0
    for i in range (2, n + 1): 
        if(l1[i]): 
            s1=s1+i 
    return s1
for _ in range(int(input())):
    n=int(input())
    s1=prime(n)
    ##print(s1)
    print(s1%10)

