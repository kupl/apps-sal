import math

def makeeql(a,o,g):
 print(abs(max(a,o) - min((min(a,o)+g),max(a,o))))
  
for i in range(int(input())):
 a,o,g = map(int,input().split())
 makeeql(a,o,g)
