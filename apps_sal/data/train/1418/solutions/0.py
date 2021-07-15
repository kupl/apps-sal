# cook your dish here
# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=list(map(int, input().split()))
 l.insert(0, 0)
 l1=[0]*(n+1)
 l1[1]=l[1]
 for i in range(2, n+1):
  l1[i]=max(l1[i-1]+l[i]*i, l1[i-2]+l[i-1]*i+l[i]*(i-1))
  
 print(l1[-1]) 
