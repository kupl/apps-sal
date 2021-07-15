t=int(input())
for _ in range(t):
 n,k=list(map(int,input().split()))
 l=list(map(int,input().split()))
 a=l[0::2]
 b=l[1::2]
 al=len(a)
 bl=len(b)
 if(al>bl):
  ll=bl
 else:
  ll=al
 b.sort()
 a.sort(reverse=True)
 i=0
 while(sum(a)>sum(b) and k>0 and i<ll):
  t=a[i]
  a[i]=b[i]
  b[i]=t
  i=i+1
  k=k-1
 if(sum(b)>sum(a)):
  print('YES')
 else:
  print('NO')

