x=int(input())
listk=[]
for i in range(0,x):
 len_s=int(input())
 build=input()
 list1=[]
 for e in build:
  list1.append(e)
 for i in range(0,len_s):
 
  if list1[i]=='1':
   
   list1[i]=='R'
   if (i-1)>=0:
    list1[i-1]='R'
   if i!=(len_s-1):
    if list1[i+1]:
     if list1[i+1]!='1':
      list1[i+1]='R'
 sum=0
 for e in list1:
  if e=='0':
   sum=sum+1
 listk.append(sum)
for e in listk:
 print(e)
  
  

