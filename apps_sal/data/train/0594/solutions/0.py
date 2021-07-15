def solve(a,n):
 max1=curr=a[0]
 for i in range(1,n):
  curr=max(a[i],curr+a[i])
  max1=max(max1,curr)
 return max1
 
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
print(sum(a)-solve(a,n)+solve(a,n)/k)

