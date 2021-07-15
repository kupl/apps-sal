# cook your dish here
import math
t=int(input())
while(t>0):
 n=int(input())
 maxProfit=-1
 for i in range(n):
  val=str(input()).split(" ")
  profit=math.floor(int(val[1])/(int(val[0])+1))*int(val[2])
  if profit>maxProfit:
   maxProfit=profit
 print(maxProfit)
 t-=1
