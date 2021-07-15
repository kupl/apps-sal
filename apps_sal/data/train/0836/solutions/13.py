for t in range(eval(input())):
 n = eval(input())
 l = list(map(int, input().split()))
 r = list(map(int, input().split()))
 lr = []
 for i in range(n):
  lr.append(l[i]* r[i])
 maxim = max(lr)
 index = -1
 maxR = -1
 for i, value in enumerate(lr):
  if maxim == value :
   if maxR < r[i]:
    maxR = r[i]
    index = i

 print(index+1)
