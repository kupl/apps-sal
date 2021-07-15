T = int(input())
for _ in range(T):
 N = int(input())
 A = list(input())
 B = list(input())
 if(not set(B).issubset(set(A))):
  print(-1)
 else:
  l1 = []
  flag = 1
  for (i,(x,y)) in enumerate(list(zip(A,B))):
   if(y>x):
    flag = 0
    break
   elif(y==x):
    pass
   else:
    l1.append((i,(x,y)))
  if(flag):
   s = set(list(reversed(list(sorted([y for i,(x,y) in l1])))))
   number_of_ops = len(s)
   print(number_of_ops)
   for char in s:
    answer = []
    for item in l1:
     if(char == item[1][1]):
      answer.append(item[0])
    answer.append(list(A).index(char))
    answer.insert(0,len(answer))
    print(' '.join(list(map(str,answer))))
  else:
   print(-1)
    
  
    

