for _ in range(int(input())):
 a, b = map(int, input().split())

 if a & 1 == 1 and b & 1 == 1:
  print((a * b) // 2 + 1)
 else:
  print((a * b) // 2)
