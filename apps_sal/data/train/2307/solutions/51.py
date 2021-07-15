def resolve():
  N, A, B = map(int, input().split(" "))
  X = [int(x) for x in input().split(" ")]

  ans = 0
  for i in range(1, N):
    walking_cost = (X[i]-X[i-1])*A
    ans += min(walking_cost, B)

  print(ans)

resolve()
