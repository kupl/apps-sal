try:
 for _ in range(int(input())):
  r,c=map(int,input().split(" "))
  x,y=map(int,input().split(" "))
  a=max((x-0),(r-x-1))
  b=max((y-0),(c-y-1))
  print(a+b)
except:
 pass
