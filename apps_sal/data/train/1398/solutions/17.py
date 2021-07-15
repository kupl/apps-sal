# cook your dish here
t=int(input())
for _ in range(t):
 arr=input()
 lis=[]
 for ele in arr:
  if ele not in lis:
   lis.append(ele)
 print(len(lis))
   
 

