import sys
from math import sqrt,gcd,log2,log10,floor,ceil,factorial
try:
 sys.stdin=open("F:\\ABHISHEK-FOLDER\\ABHI-CP\\input.txt",'r')
 sys.stdout=open("F:\\ABHISHEK-FOLDER\\ABHI-CP\\output.txt",'w')
except:
 pass

MOD = 10**9 + 7

for _ in range(int(input())):
 m , num = [int(i) for i in input().split()]
 ans = num
 perv_elee = num
 prev_val = num
 for i in range(3,2*m,2):
  curr_elee = (prev_val * perv_elee) % MOD
  curr_val = pow(curr_elee,i,MOD) 
  ans = (ans + curr_val) %MOD
  prev_val = curr_val %MOD
  perv_elee = curr_elee%MOD
 ans %= (MOD)
 print(ans)

