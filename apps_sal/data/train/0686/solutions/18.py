# cook your dish here
d = 2**0.5
for _ in range(int(input())):
 a,b,c = map(int,input().split())
 e = (2*a)/c
 s = (d*a)/b
 if e<s:
  print("Elevator")
 else:
  print("Stairs")
