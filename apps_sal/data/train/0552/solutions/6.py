t=int(input())
while(t>0):
 t-=1
 n,k=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 curr=sorted(arr)
 div1 = sum(curr[k:])-sum(curr[:k])
 div2 = sum(curr[n-k:])-sum(curr[:n-k])
 print(max(div1,div2))


