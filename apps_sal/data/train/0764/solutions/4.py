# cook your dish here
for _ in range(int(input())):
 l1=list(map(str,input().split()))
 l2=list(map(str,input().split()))
 c=0
 for i in l1:
  if i in l2:
   c=c+1 
 if c>=2:
  print('similar')
 else:
  print('dissimilar')
