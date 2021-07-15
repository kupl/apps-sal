# cook your dish here
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
t = int(input())
for _ in range(t):
 n = int(input())
 cars = get_ints()
 counter = 1
 if n == 1:
  print(1)
 else:
  min = cars[0]
  for i in range(1,n):
   if cars[i] <= min:
    counter +=1 
    min = cars[i]
  print(counter)
