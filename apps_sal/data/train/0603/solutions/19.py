# cook your dish here
x='abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
 s=''
 a=int(input())
 while 1:
  s=x[a::-1]+s
  if a<26:
   break 
  a=a-25 
 print(s)
