# cook your dish here
for _ in range(int(input())):
    n=int(input())
    k=(2*n+1)-1
    for i in range(n+1):
        a=n
        for j in range(n,i,-1):
            print(end=" ")
        for k in range(i+1):
            print(a,end="")
            a-=1
        print()
        
    for i in range(n):
        b=n
        for j in range(n+1):
            if j>i:
                print(b,end="")
                b-=1
            else:
                print(end=" ")
        print()    
            
        
        

