# cook your dish here
rii = lambda : list(map(int, input().strip().split(" ")))
ril = lambda : list(map(int, input().strip().split(" ")))
ri = lambda : int(input().strip())
rs = lambda : eval(input())
T = ri()
for _ in range(T):
 N = ri()
 l = [0 for i in range(8)]
 for i in range(N):
  nb, S = rii()
  if nb < 9:
   l[nb-1] = max(S, l[nb-1])
 print(sum(l))

