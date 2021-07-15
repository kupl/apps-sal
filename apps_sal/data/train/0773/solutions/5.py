# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<=3:
        l=[i for i in range(2,n+1)]
        l=l+[1]
        print(*l)
    elif n==4:
        print(2,1,4,3)
    elif n==5:
        print(2,1,4,5,3)
    else:
        l=[i for i in range(1,n+1)]
        if n%2==0:
            for i in range(0,n,2):
                l[i],l[i+1]=l[i+1],l[i]
            print(*l)
        else:
            for i in range(0,n-4,2):
                l[i],l[i+1]=l[i+1],l[i]
            l[-3],l[-2],l[-1]=l[-2],l[-1],l[-3]
            print(*l)
                
            

