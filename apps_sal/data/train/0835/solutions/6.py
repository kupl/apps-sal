def __starting_point():
 T = int(input())

 for i in range(T):
  N, M = list(map(int, input().split()))

  if N == 1 and M == 2:
   print("Yes")
  elif M == 1 and N == 2:
   print("Yes")
  elif N == 1 or M == 1:
   print("No")
  elif (N * M) % 2 == 0:
   print("Yes")
  else:
   print("No")

__starting_point()
