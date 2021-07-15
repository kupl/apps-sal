# cook your dish here
n=int(input())
if(n==0):
    print()
    
elif(n==1):
    print(1)
elif(n==2):
    print(2,2,2)
    print(2,1,2)
    print(2,2,2)
else:
    l=[i for i in range(1,n+1)]
    a=[]
    for i in range(2*n-1):
        a1=[]
        for i in range(2*n-1):
            a1.append(0)
        a.append(a1)
    col1=0
    coln=2*n-2
    row1=0
    rown=2*n-2
    c=n
    while(True):
        for i in range(2*n-1):
            if(a[i][col1]==0):
                a[i][col1]=c
        for i in range(2*n-1):
            if(a[i][coln]==0):
                a[i][coln]=c
        for i in range(2*n-1):
            if(a[row1][i]==0):
                a[row1][i]=c
        for i in range(2*n-1):
            if(a[rown][i]==0):
                a[rown][i]=c
        c-=1
        if(c==0):
            break
        col1+=1
        coln-=1
        row1+=1
        rown-=1
    for i in a:
        print(*i)
                
        
        

