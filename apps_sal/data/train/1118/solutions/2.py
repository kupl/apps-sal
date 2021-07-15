# cook your dish here
n=int(input())
l2=['0','1']
for i in range(n):
 s=int(input())
 w=input()
 l1=[]
 count=0
 count1=0
 for i in w:
  l1.append(i)
 l2=[]
 l3=[]
 i=1
 l2.append('1')
 l3.append('0')
 while(i<s):
  l2.append('0')
  l2.append('1')
  l3.append('1')
  l3.append('0')
  i+=1
 for i in range(s):
  if l1[i]!=l2[i]:
   count+=1
 for i in range(s):
  if l1[i]!=l3[i]:
   count1+=1
 if count>count1:
  print(count1)
 else:
  print(count)

