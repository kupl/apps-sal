for testcase in range(int(input())):
 n= int(input())
 a = [0] + list(map(int, input().split()))
 sum = [0]*(2000020)
 cnt = [0]*(2000020)
 s = 0
 ans = 0
 cnt[0] = 1
 sum[0] = 1
 for i in range(1, len(a)):
  s ^= a[i]
  ans += i*cnt[s] - sum[s]
  cnt[s] += 1
  sum[s] += i+1
 print(ans)
