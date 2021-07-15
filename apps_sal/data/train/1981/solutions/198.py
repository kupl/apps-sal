import numpy as np
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
      freq = [0]*(len(nums)+1)
      for req in requests:
        freq[req[0]] += 1
        freq[req[1]+1] -= 1
      for i in range(1, len(freq)-1):
        freq[i] = freq[i] + freq[i-1]
      freq.sort(reverse = True)
      nums.sort(reverse = True)
      return sum([x*y for x,y in zip(freq[:-1], nums)]) % (10**9+7)
