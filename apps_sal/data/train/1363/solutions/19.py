import sys

mod = 10**9 + 7;

l = [1]

for i in range(1,(10**6)+1):
 l.append((l[-1]*23)%mod)

def solve(num):
 length = len(num)
 ans = 0
 for i in range(length):
  ans += l[i] * int(num[i])
  ans %= mod
 return ans



for cases in range(int(sys.stdin.readline())):
 n,d = list(map(int,sys.stdin.readline().split()))
 num = int((str(d)*n))%mod
 num = num**2
 print(solve(str(num)))
 

