T=input()
for i in range(int(T)):
    l = list(map(int,input().split()))
    l.sort()
    if (l[2]==(l[1]**2+l[0]**2)**0.5) & (l[2]!=0) & (l[0]!=0) & (l[1]!=0): 
        print("YES")
    else:
        print("NO") 
