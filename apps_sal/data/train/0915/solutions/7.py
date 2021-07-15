for _ in range(int(input())):
 n = int(input())
 arr = list(map(int, input().split()))
 hsh = [0] * 101
 ans = 0

 for i in arr:
  if hsh[i] == 0:
   ans += 1
   hsh[i] += 1

 print(ans)
