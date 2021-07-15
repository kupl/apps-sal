def solve(n,l,r):
 ans = [0,0]
 a, b = [], []
 """if n==r and l==1:
     ans[-1] = 2**n-1
     ans[0] = n
    else:"""
 x, c, z = 1, r, l
 while c>0:
  a.append(x)
  x = x*2
  c -= 1
 x = 1
 while z>0:
  b.append(x)
  z -= 1
  x *= 2
 ans[0] = sum(b)+min(b)*(n-l)
 ans[-1] = sum(a)+max(a)*(n-r)
 return ans
def __starting_point():
 t = int(input())
 while t>0:
  t -= 1
  n, l, r = list(map(int,input().split()))
  a = solve(n,l,r)
  print(*a,sep=" ")

__starting_point()
