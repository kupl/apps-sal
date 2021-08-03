\"\"\"
0 1 2 3 4 5 6
X X X X X X X
  + + +
+ +
      + + + +

X X X X X X X
1 2 1 2 1 1 1


-1 0 1 2 3 4 5 6
   X X X X X X X
   + + + + + + +   

diff[i] : freq[i] - freq[i-1]
freq[i-1] + diff[i] = freq[i]

[1-3] [2-5]
0  1  2  3  4  5 
  +1       -1
     +1        -1 

---------------------
0  1  1  0  -1  -1  diff 
0  1  2  2   1   0

\"\"\"



class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            res += v * c
        return res % (10**9 + 7)
        
        
        
        
        
        
        
        
        
