for xxx in range(int(input(''))):
 n=int(input(''))
 a=list(map(int,input('').split(' ')))
 a=sorted(a)
 going=0
 for i in a:
  if i==0:
   going+=1 
 while 0 in a:
  a.remove(0)
 for i in range(len(a)):
  current=a[i]
  if going>=current:
   going+=1
   a[i]=-1
 print(going)
