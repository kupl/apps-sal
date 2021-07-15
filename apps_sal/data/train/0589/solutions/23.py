# cook your dish here
for _ in range(int(input())):
 p=input()
 i=0
 count=0
 result=0
 s=0
 while i<len(p):
  if p[i]=='.':
   while p[i]!='#':
    count+=1 
    i+=1 
   if result<count:
    result=count
    s+=1
   count=0
  else:
   i+=1
 print(s)

