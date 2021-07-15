try:

 for j in range(1,int(input())+1):
  n,k = map(int,input().split())

  if k>n:
   c=0
  else:
   c = n-k+1

  s = c*(c+1)//2
  print('Case', str(j)+':',s)
except:
 pass
