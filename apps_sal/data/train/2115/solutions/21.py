n,d=[int(i) for i in input().split()]
jj=[int(i) for i in input().split()]
ll=0
s=0
if n<=2:
    print(0)
    return
for i in range(n-1,1,-1):
    if jj[i]-jj[s]<=d:
        ll+=(i**2-1)*i/6
        break
for j in range(i+1,n):
    while jj[j]-jj[s]>d:
        s+=1
    ll+=(j-s)*(j-s-1)/2
print(int(ll))
