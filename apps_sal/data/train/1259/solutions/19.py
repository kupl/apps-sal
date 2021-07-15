# cook your dish here
def __starting_point():
 t=int(input())
 for m in range(t):
  l,r=list(map(int, input().split(" ")))
  co=0
  for i in range(l,r+1):
   if(i%10 == 2 or i%10==3 or i%10 == 9):
    co+=1
  print(co)
def pretty(n):
 if(n%10 == 2 or n%10==3 or n%10 == 9):
  return True
 else:
  return False
__starting_point()
