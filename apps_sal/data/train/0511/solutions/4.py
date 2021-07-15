N = int(input())
List = list(map(int,input().split()))
total = List[0]
for i in range(1,N):
  total = total^List[i]
ans = []
for i in range(N):
  ans.append(List[i]^total)
print(*ans)
