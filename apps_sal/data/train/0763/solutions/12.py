t = int(input())
for _ in range(t):
 n = int(input())
 s = input()
 p = input()
 counter = 0
 flag = 0
 count1,count2 = 0,0
 for x in s:
  if x=='1':
   count1 += 1
 for x in p:
  if x=='1':
   count2 += 1
 if count1!=count2:
  print('No')
 else:
  for i in range(n):
   if s[i]=='1' and p[i]=='0':
    counter += 1
   elif s[i]=='0' and p[i]=='1':
    counter-=1
   if counter < 0:
    flag = 1
    break
  if flag==1:
   print('No')
  else:
   print('Yes')
