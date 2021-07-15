import math

T = int(input())

#lets = 'abcdefghijklmnopqrstuvwxyz'
#key = {lets[i]:i for i in range(26)}

for t in range(T):
  #n = int(input())
  x1,y1,x2,y2 = list(map(int,input().split()))
  #a = list(map(int,input().split()))
  #a = list(input())
  d = False
  print(abs(x1-x2)+abs(y2-y1)+2*((y2!=y1)*(x2!=x1)))


