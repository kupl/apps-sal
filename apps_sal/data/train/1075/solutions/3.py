for _ in range(int(input())):
 n=int(input())
 a=[int(x) for x in input().split()]

 def nimber(game):
  if game<=2:
   return game
  mx=2
  nim=2
  while True:
   if nim==3:
    mx*=3
    mx/=2
   else:
    mx*=2
   if game<mx:
    return nim
   nim+=1
   nim%=4
  
 x=0
 for aa in a:
  x^=nimber(aa)
 if x!=0:
  print("Henry")
 else:
  print("Derek")

