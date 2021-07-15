# cook your dish here
for i in range(int(input())):
 p=input()
 l=len(p)
 arr=[0]
 count=0
 for j in range(l):
  if(p[j]=='.'):
   count=count+1
  elif(count>0 and p[j]=='#'):
   if(max(arr)<count):
    arr.append(count)
   count=0
 print(len(set(arr))-1)
