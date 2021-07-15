l=input()
n=int(input())
for i in range(n):
 flag=0
 s=input()
 for j in range(len(s)):
  if(s[j] in l):
   flag=flag+1
 if(flag==len(s)):
  print("Yes")
 else:
  print("No")
