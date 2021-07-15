# cook your dish here
refList=[1,2,3,4,5,6,7]
t=int(input())
for i in range(t):
 a=int(input())
 list1=list(map(int,input().split()))[:a]
 sevenInt=[]
 revList=list1[::-1]
 for i in list1:
  if i not in sevenInt:
   sevenInt.append(i)
 if(sevenInt==refList and list1==revList):
  print('yes')
 else:
  print('no')
