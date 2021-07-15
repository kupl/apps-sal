# cook your dish here
t=int(input())
po=0
ne=0
for i in range(t):
    s,n,k,r=list(map(int,input().split()))
    sum=0
    for j in range(n):
        sum=sum+k
        k=k*r
    if(s>=sum):
        remaining_slices=s-sum
        print("POSSIBLE",remaining_slices)
        po=po+remaining_slices
    else:
        remaining_slices=sum-s
        print("IMPOSSIBLE",remaining_slices)
        ne=ne+remaining_slices
#print(po,ne)
if(po>=ne):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

