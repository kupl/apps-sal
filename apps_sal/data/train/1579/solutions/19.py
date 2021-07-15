# cook your dish here
def solve(A): 
 res, pre=set(),{0}
 for x in A: 
  pre={x|y for y in pre}|{x} 
  res|=pre 
 return len(res) 
 
test=int(input())
for _ in range(test):
 n=int(input())
 arr=list(map(int,input().split()))
 if(solve(arr)!=n*(n+1)//2):
  print('NO')
 else:
  print('YES')

