t=int(input())

while t>0:
    t-=1
    n=int(input())
    
    l1=[int(i) for i in input().split(" ")]
    
    ans=""
    
    flag=0
    k=0
    for i in l1:
        if flag==1 and i!=1:
            k+=1
        elif i==1 and flag==0:
            flag=1
        elif i==1 and flag==1:
            if k>=5:
                k=0
            else:
                ans="NO"
                break
    if ans=="":
        ans="YES"
    print(ans)
            
