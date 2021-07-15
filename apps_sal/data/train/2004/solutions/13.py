a=input()
i=0
while i<len(a):
 if a[i]=='0':
  print(a[:i]+a[i+1:])
  break
 i+=1
 if i==len(a):print('1'*(len(a)-1))

