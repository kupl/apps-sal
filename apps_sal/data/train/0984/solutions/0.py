t = int(input())
for i in range(t):
 n = int(input())
 l = list(map(int, input().split()))
 counter = 0
 even = 0
 for num in l:
  if num % 2 == 0:
   even += 1 
  if num % 2 == 1:
   counter += even
 print(counter)
 

