# cook your dish here
try:
    t=int(input())
    l=[]
    flag=0
    for k in range(0,t):
        n,m=(int(i) for i in input().split(" "))
        l.append([n,m])
    for i in range(0,t):
        s=l[i][0]+l[i][1]
        for j in range(i+1,t):
            if(s==l[j][0] and l[i][0]==(l[j][0]+l[j][1])):
                flag=1
                print("YES")
                break
    if(flag==0):
        print("NO")
            
except:
    pass
