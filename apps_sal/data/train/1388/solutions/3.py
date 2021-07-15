def solve(n):
 total=n
 tax=0
 if n>1500000:
  tax+=(n-1500000)*(0.30)
  n=1500000
 if n>1250000:
  tax+=(n-1250000)*(0.25)
  n=1250000
 if n>1000000:
  tax+=(n-1000000)*(0.20)
  n=1000000
 if n>750000:
  tax+=(n-750000)*(0.15)
  n=750000
 if n>500000:
  tax+=(n-500000)*(0.10)
  n=500000
 if n>250000:
  tax+=(n-250000)*(0.05)
 return int(total-tax)
for _ in range(int(input())):
 n=int(input())
 print(solve(n))
