# cook your dish here
P = [True]*1001
p = 2
while p*p<=201:
    for i in range(p*p,1001,p):
        P[i]=False
    p+=1
sp = [False]*1010
for i in range(2,1001):
    j=i+1
    while i*j<=1000:
        if P[i]==True and P[j]==True:
            sp[i*j]=True
        j+=1
for t in range(int(input())):
    n = int(input())
    ok = False
    for i in range(2,n):
        if sp[i]==True and sp[n-i]==True:
            ok = True
            break
    if ok==False:
        print("NO")
    else:
        print("YES")
