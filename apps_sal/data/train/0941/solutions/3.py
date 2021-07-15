# cook your dish here
t = int(input())

for i in range(t):
 a,b = list(map(int,input().split()))
 
 count=0

 if a % 2 != 0:
  even_x = a//2
  odd_x = a//2 +1
 else:
  even_x = a//2
  odd_x = a//2
  
 if b % 2 !=0:
  even_y = b//2
  odd_y = b//2 +1
 else:
  even_y = b//2
  odd_y = b//2
  
 count = (even_x * even_y) + (odd_x * odd_y)
 
 print(count)

