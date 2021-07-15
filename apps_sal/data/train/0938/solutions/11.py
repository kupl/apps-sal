for _ in range(eval(input())):
 n = eval(input())
 l = list(map(int, input().split()))
 c = 0
 for i in range(n):
  for j in range(i, n):
   for k in range(i):
    for m in range(k, i):
     c+=len(set(l[i:j+1])&set(l[k:m+1]))==0
 print(c)
