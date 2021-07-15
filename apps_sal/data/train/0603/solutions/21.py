x = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
 num = int(input())
 r = ''
 while 1:
  r = x[num::-1]+r
  if num<26:
   break
  num-=25
 print(r)

