# cook your dish here
import sys

mod_val = 1000000007
rang = [0]*101
pow_cache = [0]*102
multisets = {}


def mod_pow(base, pow):
 result = 1
 while pow:
  if pow&1:
   result = (result*base) % mod_val
  base = (base*base) % mod_val
  pow = pow>>1
 return result


def precalculate():

 for i in range(1, 102):
  pow_cache[i] = mod_pow(i, mod_val-2)


def cal_recurse(i, target_sum):
 if target_sum == 0:
  return 1
 if i>=target_sum:
  return 0
 if (i, target_sum) in multisets:
  return multisets[(i, target_sum)]
 ans = cal_recurse(i+1, target_sum)
 max_pos = target_sum//(i+1)
 choose = rang[i+1]%mod_val
 for j in range(1, max_pos+1):
  temp = choose*cal_recurse(i+1, target_sum-j*(i+1))
  # temp%=mod_val
  ans += temp
  ans %= mod_val
  choose *= rang[i+1]+j
  # choose %= mod_val
  choose *= pow_cache[j+1]
  choose %= mod_val
 multisets[i, target_sum] = ans
 return ans


def calculate(target_sum, rang_index):
 populate(target_sum, rang_index)
 return cal_recurse(0, target_sum)


def populate(target_sum, rang_i):
 for i in range(1, target_sum+1):
  rang[i] = rang_i[0] + (rang_i[1] + (rang_i[2] + rang_i[3]*i)*i)*i


_test_cases = int(input())
precalculate()
for _a_case in range(_test_cases):
 rang = [0]*101
 multisets = {}
 _rang_index = [int(i) for i in input().split(' ')]
 _target_sum = int(input())
 print(calculate(_target_sum, _rang_index))

