# cook your dish here
t=int(input())
w=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    Q=int(input())
    for j in range(Q):
        q=list(map(int,input().split()))
        count=0
        for k in range(q[0],q[1]+1):
            count+=a[k-1]
        w.append(count)
for i in w:
    print(i)



