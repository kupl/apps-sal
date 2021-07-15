# cook your dish here
t = int(input())
for _ in range(t):
 m,n = [int(d) for d in input().split()]

 if m == 1:
  arr = []
  if n%4 == 0:
   print(2)
   arr = [[1,1,2,2]*(n//4)]
  elif n%4 == 1:
   if n == 1:
    print(1)
    arr = [[1]]
   else:
    print(2)
    arr = [[1,1,2,2]*(n//4) + [1]]
  elif n%4 == 2:
   if n == 2:
    print(1)
    arr = [[1,1]]
   else:
    print(2)
    arr = [[1,1,2,2]*(n//4) + [1,1]]
  elif n%4 == 3:
   print(2)
   arr = [[1,1,2,2]*(n//4) + [1,1,2]]

 elif m == 2:
  if n%3 == 0:
   print(3)
   a1 = [1,2,3]*(n//3)
   arr = [a1,a1]

  elif n%3 == 1:
   if n == 1:
    print(1)
    arr = [[1],[1]]
   else:
    print(3)
    a1 = [1,2,3]*(n//3) + [1]
    arr = [a1,a1]

  elif n%3 == 2:
   if n == 2:
    print(2)
    arr = [[1,2],[1,2]]
   else:
    print(3)
    a1 = [1,2,3]*(n//3) + [1,2]
    arr = [a1,a1]

 elif m == 3:
  if n == 1:
   print(2)
   arr = [[1],[1],[2]]
  elif n == 2:
   print(3)
   arr = [[1,1],[2,2],[3,3]]
  elif n == 3:
   print(4)
   arr = [[1,3,4],[4,2,1],[4,2,1]]
  elif n == 4:
   print(4)
   arr = [[1,3,4,2],[4,2,1,3],[4,2,1,3]]
  else:
   if n%4 == 0:
    print(4)
    a1 = [1,3,4,2]*(n//4)
    a2 = [4,2,1,3]*(n//4)
    arr = [a1,a2,a2]
 
   elif n%4 == 1:
    print(4)
    a1 = [1,3,4,2]*(n//4) + [1]
    a2 = [4,2,1,3]*(n//4) + [4]
    arr = [a1,a2,a2]

   elif n%4 == 2:
    print(4)
    a1 = [1,3,4,2]*(n//4) + [1,3]
    a2 = [4,2,1,3]*(n//4) + [4,2]
    arr = [a1,a2,a2]

   elif n%4 == 3:
    print(4)
    a1 = [1,3,4,2]*(n//4) + [1,3,4]
    a2 = [4,2,1,3]*(n//4) + [4,2,1]
    arr = [a1,a2,a2]

 else:
  if n == 1:
   print(2)
   a1 = [1,3,4,2]*(n//4) + [1]
   a2 = [4,2,1,3]*(n//4) + [2]
   arr = []
   i = 0
   j = 0
   c = 0
   c1 = 0
   for i in range(m):
    if j == 0 and c < 3:
     arr.append(a1)
     c = c + 1
     if c == 2:
      j = 1
      c = 0
    else:
     arr.append(a2)
     c1 = c1 + 1
     if c1 == 2:
      j = 0
      c1 = 0
  
  elif n == 2:
   print(3)
   arr = []
   a1 = [1,1]
   a2 = [2,2]
   a3 = [3,3]

   if m%3 == 1:
    arr = [a1,a2,a3]*(m//3) + [a1]
   elif m%3 == 2:
    arr = [a1,a2,a3]*(m//3) + [a1,a2]
   elif m%3 == 0:
    arr = [a1,a2,a3]*(m//3)

  else:
   print(4)
   if n%4 == 0:
    a1 = [1,3,4,2]*(n//4)
    a2 = [4,2,1,3]*(n//4)
    arr = []
    i = 0
    j = 0
    c = 0
    c1 = 0
    for i in range(m):
     if j == 0 and c < 3:
      arr.append(a1)
      c = c + 1
      if c == 2:
       j = 1
       c = 0
     else:
      arr.append(a2)
      c1 = c1 + 1
      if c1 == 2:
       j = 0
       c1 = 0

   elif n%4 == 1:
    a1 = [1,3,4,2]*(n//4) + [1]
    a2 = [4,2,1,3]*(n//4) + [4]
    arr = []
    i = 0
    j = 0
    c = 0
    c1 = 0
    for i in range(m):
     if j == 0 and c < 3:
      arr.append(a1)
      c = c + 1
      if c == 2:
       j = 1
       c = 0
     else:
      arr.append(a2)
      c1 = c1 + 1
      if c1 == 2:
       j = 0
       c1 = 0

   elif n%4 == 2:

    a1 = [1,3,4,2]*(n//4) + [1,3]
    a2 = [4,2,1,3]*(n//4) + [4,2]
    arr = []
    i = 0
    j = 0
    c = 0
    c1 = 0
    for i in range(m):
     if j == 0 and c < 3:
      arr.append(a1)
      c = c + 1
      if c == 2:
       j = 1
       c = 0
     else:
      arr.append(a2)
      c1 = c1 + 1
      if c1 == 2:
       j = 0
       c1 = 0

   elif n%4 == 3:

    a1 = [1,3,4,2]*(n//4) + [1,3,4]
    a2 = [4,2,1,3]*(n//4) + [4,2,1]
    arr = []
    i = 0
    j = 0
    c = 0
    c1 = 0
    for i in range(m):
     if j == 0 and c < 3:
      arr.append(a1)
      c = c + 1
      if c == 2:
       j = 1
       c = 0
     else:
      arr.append(a2)
      c1 = c1 + 1
      if c1 == 2:
       j = 0
       c1 = 0



 for i in range(m):
  for j in range(n):
   print(arr[i][j],end = " ")
  print()




    
    














