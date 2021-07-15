t=int(input())
while(t):
    n=int(input())
    p=int(n/2)
    p=p+1
    for i in range(0,p):
        for j in range(0,i):
            if(j>=0):
                print(end=" ")
        print("*")
    p=p-2
    for i in range(p,0,-1):
        for j in range(0,i):
            print(end=" ")
        print("*")
    
    if(n>1):
        print("*")
    t=t-1

