# cook your dish here
N = int(input())
cnt = 0
for _ in range(N):
  arr = list(map(int,input().split()))
  if arr.count(1) >= 2:
   cnt += 1
print(cnt)
