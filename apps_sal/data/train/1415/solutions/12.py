def palindrome(ch):
 t=False
 if ch==ch[::-1]:
  t=True
 return t
def deel(ch,i):
 gh=ch[:i]+ch[i+1:]
 return gh
for i in range(int(input())):
 ch=input()
 f=0
 for j in range(len(ch)):
  
  gh=deel(ch,j)
  if palindrome(gh):
   f=1
   print('YES')
   break
 if f==0:
  print('NO')
  

