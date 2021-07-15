# cook your code here
zz= int(input(''))
for j in range(zz):
 xx=int(input(''))
 x=list(input(''))
 kk=0
 sos=''
 for i in range (xx,0,-4):
  t=3
  c=0
  for k in range (4):
   c=c+(int(x[kk])*(2**t))
   kk=kk+1
   t=t-1
  sos=sos+ chr(c+97)
 print(sos)
