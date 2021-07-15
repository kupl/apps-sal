t=int(input())
for i in range(t):
 list1=list(map(int,input().split()))
 s=list1[0]
 list2=list1[1:]
 if(sum(list2)<=list1[0]):
  print("1")
 else:
  
  if(list2[0]+list2[1]<=s and list2[2]<=s):
   print("2")
  elif(list2[2]+list2[1]<=s and list2[0]<=s):
   print("2")
  elif(list2[0]<=s and list2[1]<=s and list2[2]<=s):
   print("3")
