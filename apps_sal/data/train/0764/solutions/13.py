for i in range(int(input())):
 l=[]
 l=input().split()
 k=[]
 k=input().split()
 k.sort()
 l.sort()
 c=0
 for j in l:
  for m in k:
   if j==m:
    c+=1
 if(c>=2):
  print('similar')
 else:
  print('dissimilar')
