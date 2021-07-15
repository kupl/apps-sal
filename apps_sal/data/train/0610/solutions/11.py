# cook your dish here
for T in range(int(input())):
    n = int(input())
    ls = list(map(int,input().split()))
    flag1 = 0
    lr = []
    for i in range(n):
        if ls[i]==1:
            lr.append(i+1)
    # print(lr)
    if len(lr)==1:
        print("YES")
    else:
        for j in range(1,len(lr)):
            if (lr[j]-lr[j-1])>=6:
                flag1 = 1 
            else:
                flag1 = 0 
                break
            
        if flag1==1:
            print("YES")
        else:
            print("NO")
            
