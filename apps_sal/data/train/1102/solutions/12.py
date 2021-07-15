# cook your dish here
d={'2':3,'3':3,'4':3,'5':3,'6':3,'7':4,'8':3,'9':4}
mod=10**9+7
try:
 t=int(input())
 while(t):
  mul=1
  s=int(input())
  s=str(s)
  s=sorted(s)
  for i in s:
   mul=mul*(d[i])
  print(mul%mod)
  t=t-1
except EOFError:
 pass

