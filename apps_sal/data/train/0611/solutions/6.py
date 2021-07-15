for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 ans="Poor Chef"
 sa=set(a)
 l=[a[i-1] for i in a]
 sb=set(l)
 if len(sa)>len(sb):
  ans="Truly Happy"
 print(ans)
