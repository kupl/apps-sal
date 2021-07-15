for _ in range(int(input())):
 num = int(input())
 
 moves = 0
 x,y = 0,0
 
 while x<=num:
  x = int(y**0.5)+1
  y += x*x
  moves += 1

 print(moves-1)

