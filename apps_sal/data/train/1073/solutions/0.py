import sys
def fin(): return sys.stdin.readline().strip()
def fout(s, end="\n"): sys.stdout.write(str(s)+end)

MOD = pow(10, 9)+7
t = int(input())
while t>0:
 t -= 1
 n, m = list(map(int, fin().split()))
 if n == 1:
  print(m%MOD)
  continue
 dp1 = m*(m-1)
 dp2 = m
 for i in range(3, n+1):
  temp = dp2
  dp2 = dp1 
  dp1 = (temp*(m-1))%MOD+(dp1*(m-1))%MOD
 print((dp1+dp2)%MOD)

 


