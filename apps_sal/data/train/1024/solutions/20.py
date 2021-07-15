list1=[]
t=int(input())
for i in range(t):
    s,n,k,r=list(map(int,input().split()))
    p=0
    for i in range(n):
        a=r**i
        p=p+a*k
    c=s-p
    list1.append(c)
    if s>=p:
        print("POSSIBLE {0}".format(c))   
    else:
        print("IMPOSSIBLE {0}".format(abs(c)))
s=0
for j in range(len(list1)):
    s+=list1[j]
if s==0 or s>0:
    print("POSSIBLE")    
else:
    print("IMPOSSIBLE")

