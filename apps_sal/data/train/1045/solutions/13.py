t = int(input())
mod = 10**9 + 7
for _ in range(t):
 s = input().strip()
 ss = ''
 for x in s:
  if x in ['a', 'e', 'i', 'o', 'u']:
   ss += '0'
  else:
   ss += '1'

 ans = 0
 print(int(ss, 2)%mod)
 # for i in range(len(ss)-1, -1, -1):
 #   if ss[i] == '1':
 #       ans += pow(2, len(ss)-1-i, mod)
 # print(ans%mod)

