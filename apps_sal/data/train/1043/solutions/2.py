t=int(input())
for i in range(t):
 n,k=list(map(int,input().split()))
 strings=input().split()
 res=""
 for i in range(k):
  modernlanguage=input().split()
  modernlanguage.remove(modernlanguage[0])
  res=res+"".join(modernlanguage)
 res1=[]
 for i in range(len(strings)):
  if(strings[i] in res):
   res1.append("YES")
  else:
   res1.append("NO")
 print(*res1)
 
  

