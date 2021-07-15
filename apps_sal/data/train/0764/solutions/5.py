for _ in range(int(input())):
 s1=input().split()
 s2=input().split()
 count=0
 for i in s1:
  for j in s2:
   if i==j:
    count+=1
 if count>=2:
  print('similar')
 else:
  print('dissimilar')
