n = eval(input())
gr = [int(i) for i in input().split()]
q = eval(input())
for _ in range(q):
 l,r = list(map(int,input().split()))
 temp = gr[l-1:r]
 temp.sort()
 ans = 0
 l = len(temp)
 for i in range(l-1):
  x = temp[i]
  y = temp[i+1]
  ans += (x-y)*(x-y)
 print(ans)

