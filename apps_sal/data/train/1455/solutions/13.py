import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

for cases in range(int(sys.stdin.readline())):
 L, R = list(map(int,sys.stdin.readline().split()))
 List = sorted(l[L-1:R])
 ans = 0
 for i in range(1,len(List)):
  ans += (List[i]-List[i-1])**2
 print(ans) 

