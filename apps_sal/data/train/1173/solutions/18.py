from collections import defaultdict
def solve(C,N):
 cnt=defaultdict(list)
 cnt[0].append(-1)
 r=0
 for i in range(len(C)):
  r=r^C[i]
  cnt[r].append(i)
 res=0
 for l in cnt:
  x=len(cnt[l])-1
  neg=x
  y=0
  for k in range(len(cnt[l]))[::-1]:
   y+=x*cnt[l][k]-neg
   x-=2 
   neg-=1
  res+=y
 return res

def main():
 for _ in range(int(input())):
  N=int(input())
  C=list(map(int,input().split()))
  print(solve(C,N))
main()
