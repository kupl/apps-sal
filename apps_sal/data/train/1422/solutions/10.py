cases = int(input())
for case in range (cases):
 length = int(input())
 buildings = [1]*length
 bombs = input()
 for i in range(length):
  if (bombs[i]=="1"):
   buildings[i] = 0
   if (i!=0):
    buildings[i-1] = 0
   if (i!=length-1):
    buildings[i+1] = 0
   i = i+2
 print(buildings.count(1))

