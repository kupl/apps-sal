t=int(input())
for i in range(t):
    k=int(input())
    a=1
    for i in range(1,k+1):
        b=a+i
        l=[]
        for x in range(a,b):
            l.append(x)
        for y in l[::-1]:
            print(y,end="")
        print()    
        a=b    
        

