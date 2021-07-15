# cook your dish here
for _ in range(int(input())):
    k=int(input())
    whole=2*k+1
    half=int(whole/2)
    l=[]
    for i in range(k,-1,-1):
        l.append(i)
    print(k)
    for i in range(1,half):
        for j in range(0,i+1):
            print(l[j],end="")
        print()
    print(*l,sep="")
    for i in range(half,-1,-1):
        for j in range(0,i):
            print(l[j],end="")
        print()
        
    
            
    
            
        
        
    
        
        

