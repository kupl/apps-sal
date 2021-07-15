# cook your dish here
MOD = 998244353

fball = [ [0]*101 for _ in range(101) ]

cric = [ [0]*101 for _ in range(101) ] 



def calSNum(n, r):
 if n == r or r == 1:
  fball[r][n] = 1
  return
 if n > 0 and r > 0 and n > r:
  fball[r][n] = (fball[r-1][n-1]%MOD + (r*fball[r][n-1])%MOD )%MOD
  return
 fball[r][n] = 0
  

def calASNum(n, r):
 if n == 0 and r == 0 :
  cric[r][n] = 0
  return
 if n >= 2 and r == 1:
  cric[r][n] = 1
  return 
 if r > 0 and n > 0 and n >= 2*r:
  cric[r][n] = ((r*cric[r][n-1])%MOD + ((n-1)*cric[r-1][n-2])%MOD )%MOD
  return
 cric[r][n] = 0
 

def preCompute():
 for r in range(1,101):
  for n in range(1, 101):
   calSNum(n, r)
   calASNum(n, r)

 
def main():
 
 preCompute()
 for _ in range(int(input())):
  f, c, r = list(map(int, input().split()))

  ans = 0
  
  if f + (c//2) >= r:
   minv = min(f, r)
   
   for i in range(1, minv+1):
    if r-i <= c//2:
     ans = (ans + (fball[i][f] * cric[r-i][c])%MOD )%MOD
   
  print(ans)
   
def __starting_point():
 main()

__starting_point()
