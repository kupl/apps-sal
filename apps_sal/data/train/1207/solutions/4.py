# cook your dish here
t=0
try:
 t=int(input())
except:
 pass

for _ in range(t):
 
 n= int(input())
 p=list(map(int, input().split()))
 
 middle = min(p)
 p.remove(middle)
 cost =0
 for i in p:
  cost+= i*middle
 print(cost)
