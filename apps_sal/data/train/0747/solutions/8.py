# cook your dish here
t = int(input())
while t:
 n = int(input())
 li = [int(x) for x in input().split()]
 l = [0 for i in range(max(li)+1)]
 for i in range(len(li)):
  l[li[i]] = l[li[i]]+1
 if max(l)>=3:
  print("NO")
 elif l[max(li)]>=2:
  print("NO")
 else:
  print("YES")
  for j in range(len(l)):
   if l[j]>=1:
    print(j,end = ' ')
    l[j] = l[j]-1
  for j in range(len(l)-1,-1,-1):
   if l[j]>=1:
    print(j,end = ' ')
    l[j] = l[j]-1
 print()
   
     
 t = t-1
