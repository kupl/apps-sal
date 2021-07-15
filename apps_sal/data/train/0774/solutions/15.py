def solve():
 n, k, p = list(map(int, input().split()))
 arr = list(map(int, input().split()))
 new = []
 for i in range(n):
  new.append([arr[i], i])
 new1 = sorted(new, key=lambda x: x[0])
 po = 0
 store = [0] * n
 for i in range(1, n):
  if (new1[i][0] - new1[i - 1][0]) > k:
   po += 1
  store[new1[i][1]] = po
 for i in range(p):
  p1, p2 = list(map(int, input().split()))
  if store[p1 - 1] == store[p2 - 1]:
   print("Yes")
  else:
   print("No")


def __starting_point():
 solve()

__starting_point()
