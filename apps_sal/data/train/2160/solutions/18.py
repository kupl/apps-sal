n,k=map(int,input().split())
l=list(map(int,input().split()))
if 1==k :
    print("Yes")
    print(n)
    return
su = sum(l)
if su%k!=0 :
    print("No")
    return
k1=su//k
t=0
k2=0
j1=[]
for i in l :
    t=t+i
    k2+=1
    if t == k1 :
        j1.append(k2)
        k2=0
        t=0
    if t > k1 :
        print("No");return
print("Yes")
print(*j1)
