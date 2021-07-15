# cook your dish here
for a0 in range(int(input())):
 n=int(input())
 s,x="",""
 k=input()
 for i in range(n):
  s+=str((i+1)%2)
  x+=str(i%2)
 hee,hoo=0,0
 for i in range(n):
  if k[i]!=s[i]:
   hee+=1
  if k[i]!=x[i]:
   hoo+=1
 print(min(hee,hoo))
