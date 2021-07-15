# cook your dish here
for _ in range(int(input())):
 n = int(input())
 lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
 f = lst
 o = ''
 fo = ''
 s = input()
 for i in range(n+1):
  if i%4==0:
   fo+=o
   f = lst
  if i==n:
   break
  if int(s[i])==0:
   f = f[:len(f)//2]
   o = f[0]
  elif int(s[i])==1:
   f = f[len(f)//2:]
   o = f[0]
 print(fo)

