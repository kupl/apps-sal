t=int(input())
while t>0:
 n,k=map(int,input().split(" "))
 li=list(map(int,input().split(" "))) 
 li.sort()
 h=n//2
 if n%2!=0:
  h+=1 
 if k>=h:
  k=n-k
 l1=li[:k]
 l2=li[k:]
 #print(l1,l2)
 print(abs(sum(l1)-sum(l2)))
 t-=1
