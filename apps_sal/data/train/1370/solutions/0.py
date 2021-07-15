for _ in range(int(input())):
 k, n = input().split()

 while int(n) >= 5:
  print(len(set(k)) ** 3)
  break
