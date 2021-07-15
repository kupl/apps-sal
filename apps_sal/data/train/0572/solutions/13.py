for _ in range(int(input())):
 x, y, z= map(int, input().split())
 if abs(x-y)<=z:
  print(0)
 else:
  print(abs(x-y)-z)
