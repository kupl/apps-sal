# cook your dish here
t = int(input())

for e in range(t):
 n = int(input())

 if n % 2 == 0:
  print("NO")
 else:
  print("YES")

  total = 0
  for g in range(n):
   total += g
  num = total // n
  
  for i in range(n):
   l = [0] * n
   for j in range(i+1, i+1+num):
    try:
     l[j] = 1
    except IndexError:
     k = j - n
     l[k] = 1
   for b in range(len(l)):
    print(l[b], end = "")
    
   print()

