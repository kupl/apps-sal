# cook your dish here
t = int(input())
tp = [];
tp.append(0)
tp.append(1)
for i in range(2,5050):
 tp.append(tp[i-1]+tp[i-2])
for i in range(t):
 n = int(input())
 c = 0
 for j in range(1,n+1):
  for k in range(1,j+1):
   print(tp[c],sep = ' ',end=' ')
   c += 1;
  print() 
 
