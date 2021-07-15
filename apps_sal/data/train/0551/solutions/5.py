# cook your dish here
for _ in range(int(input())):
 s=input()
 flag=0
 for i in range(len(s)):
  if s.count(s[i]) > 1:
   flag=1
   break
 if flag==1:
  print('yes')
 else:
  print('no')
