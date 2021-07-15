# cook your dish here
sieve=[True for i in range(201)]
sieve[0],sieve[1]=False,False
i=2
p=[]
while i<=200:
    if sieve[i]:
        p.append(i)
        j=i*i
        while j<=200:
            sieve[j]=False
            j+=i
    i+=1
l=len(p)
semi=[]
for i in range(l):
    for j in range(i+1,l):
        if p[i]*p[j]<=200:
            semi.append(p[i]*p[j])
semi=set(semi)
for _ in range(int(input())):
    n=int(input())
    i=1
    out=False
    while i<=100:
        if i in semi and n-i in semi:
            print('YES')
            out=True
            break
        i+=1
    if not out:
        print("NO")
        
