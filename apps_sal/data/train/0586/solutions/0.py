# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    a=[]
    sr=[]
    for i in range(k):
        x,y=input().split()
        y=int(y)
        a.append([10**10-y,x])
        sr.append(sorted(x))
    for i in range(n-k):
        x,y=input().split()
        y=int(y)
        x=sorted(x)
        for j in range(k):
            if x==sr[j]:
                a[j][0]-=y
                break
    a.sort()
    for i in a:
        print(i[1],abs(i[0]-10**10))
