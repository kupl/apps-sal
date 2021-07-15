n,k=[int(x) for x in input().split()]
a=[]
res=[]
for _ in range(n):
    a.append(int(input()))
a.sort()  
# print(a)
for _ in range(n-k+1): 
    res.append(abs(a[_]-a[_+k-1]))
print(min(res))

