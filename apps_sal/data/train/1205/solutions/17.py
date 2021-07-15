a=int(input())
answer=[]
for i in range(a):
 s=input()
 l=len(s)
 ans=0
 for i in range(l-1):
  if s[i]==s[i+1]:
   ans=ans+((l-1)*l)/2
  elif s[i]!=s[i+1]:
   ans=ans+l
 answer.append(ans) 
for i in range(a):
 print(int(answer[i]))
