for _ in range(int(input())):
 R, G, B, M = map(int, input().split())
 R_list = list(map(int, input().split()))
 G_list = list(map(int, input().split()))
 B_list = list(map(int, input().split()))
 for j in range(M):
  rSum = max(R_list)
  gSum = max(G_list)
  bSum = max(B_list)
  p = max(rSum, bSum, gSum)
  if p == rSum:
   for i in range(R):
    R_list[i] = R_list[i] // 2
  elif p == bSum:
   for i in range(B):
    B_list[i] = B_list[i] // 2
  else:
   for i in range(G):
    G_list[i] = G_list[i] // 2
 rSum = max(R_list)
 gSum = max(G_list)
 bSum = max(B_list)
 print(max(rSum, bSum, gSum))
