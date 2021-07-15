import re

class arrSol():
 def __init__(self):
  self.N = 0
  self.arr = 0
 
 def updateN(self, N):
  self.N = N

 def populateArr(self):
  self.arr = input()
  self.arr = re.split(" ", self.arr)
  
 def findCost(self):
  min = 100001
  for i in range(self.N):
   if int(self.arr[i]) < min:
    min = int(self.arr[i])
  return min * (self.N - 1) 
  
  
  


T = int(input())

for i in range(T):
 
 myObj = arrSol()
 myObj.updateN(int(input()))
 myObj.populateArr()
 print(int(myObj.findCost()))
 del myObj
 

