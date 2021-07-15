# cook your dish here
t = int(input())
for _ in range(t):
 s = input().split(' ')
 flag = 0
 if(s[0]==s[2]):
  if(s[0]==s[4] or s[0]==s[5]):
   flag = 1
 if(s[0]==s[3]):
  if(s[0]==s[4] or s[0]==s[5]):
   flag = 1
 if(s[1]==s[2]):
  if(s[1]==s[4] or s[1]==s[5]):
   flag = 1
 if(s[1]==s[3]):
  if(s[1]==s[4] or s[1]==s[5]):
   flag = 1
 if(flag==0):
  print('NO')
 else:
  print('YES')
