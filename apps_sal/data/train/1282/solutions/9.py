# Ankan Kumar Das
# Date : 27/02/2020
MOD = 10**9 + 7
for _ in range(int(input())):
 l, r = map(int, input().split())
 max_no_elm = r - l + 1
 ans, multi, l_p, r_p = 0, 1, l, 0
 while l_p != 0:
  curr_bit = l_p & 1
  if curr_bit == 1:
   no_elm = multi - r_p
   ans = (ans + multi * min(no_elm, max_no_elm)) % MOD
  l_p, r_p = l_p >> 1, r_p + multi * curr_bit
  multi = multi << 1
 print(ans)
