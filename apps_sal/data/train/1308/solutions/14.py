try:
 while True:
  password=list(input().strip())
  temp=password[:]
  for i in password:
   if i.isdigit():
    temp.remove(i)
  password1=set(temp)
  #print password1,temp
  if len(password1)!=len(temp):
   print('Invalid')
  else:
   print('Valid')
   4/0
except:
 return

