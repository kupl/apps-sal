t = eval(input())
while t>0:
 n = eval(input())
 ar = list(map(int,input().split()))
 c = 0
 for i in range(0,n):
  for j in range(i,n):
   for k in range(j+1,n):
    for l in range(k,n):
     res = []
     res = list(set(ar[i:j+1]).intersection(set(ar[k:l+1])))
     #print ar[i:j+1], ar[k:l+1]
     if len(res)==0:
      c+=1
 print(c)
 t-=1 
