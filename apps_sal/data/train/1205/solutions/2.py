t=int(input())
for _ in range(t):
 s=input()
 n=len(s)
 hak=0
 
 for i in range(n-1):
  if(s[i]==s[i+1]):
   hak+=1
   
 red=(hak*n*(n+1))
 red=red//2
 clu=n*n
 qwe=2*hak*n
 print(red+clu-qwe-n)
