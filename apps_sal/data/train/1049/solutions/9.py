for ts in range(int(input())):
 n,k=map(int,input().split())
 l=list(map(int,input().split()))
 c=len(set(l))
 su=[]
 for i in range(n-k+2):
  if len(set(l[i:i+k]))==c:
   su.append(sum(l[i:i+k]))
  else:
   pass
 print(max(su))
