t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    cou=0
    for j in range(n-2):
        a1=l[j]
        a2=l[j+1]
        a3=l[j+2]
        if(a1==a2 and a2==a3):
            flag=1
            break
    if(flag==1):
        print("Yes")
    else:
        print("No")
        


