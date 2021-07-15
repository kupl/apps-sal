n = int(input())
l = []
ll =[]
ans=[]
for i in range(n):
    x = int(input())
    l.append(x)
for i in range(n) :
    for j in range(i+1,n):
        if l[j] - l[i] > 0 :
            ll.append(l[j]-l[i])
        else:
            ll.append(l[i]-l[j])
ll.sort()
for i in range(2,int(ll[0]**0.5)+1):
    if i * i > ll[0] :
        break
    if ll[0] % i == 0 :
        ans.append(i)
        ans.append(ll[0]//i)
ans.append(ll[0])
ans = list(set(ans))
ans.sort()
print(*ans)
        


