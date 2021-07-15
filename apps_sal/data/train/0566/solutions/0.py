t=int(input())
for _ in range (t):
 str1=input()
 str2=input()
 res='No'
 for i in str1:
  if i in str2:
   res='Yes'
   break
 print(res)

