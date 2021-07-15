nl = list(map(int,input().split()))
N = nl[0]
L = nl[1]
ss = [input() for i in range(N)]
ss.sort()
res = ""
for i in ss:
  res = res+i
print(res)
