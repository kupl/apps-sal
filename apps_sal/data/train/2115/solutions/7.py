n,d=[int(i) for i in input().split()]
q=list(map(int, input().split()))
s=0
if n<3:
    print(0)
else:
    t=3
    for i in range(n-2):
        for j in range(i+t-1,n):
            if q[j]-q[i]>d:
                j-=1
                break
        t=j-i
        s+=t*(t-1)//2
    print(s)

