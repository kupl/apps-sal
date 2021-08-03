class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n, m = len(nums), len(requests)
        count = [0 for _ in range(n + 1)]
        for begin, end in requests:  
            count[begin] += 1
            count[end + 1] -= 1
        for i, c in enumerate(count):
            if i != 0:
                count[i] += count[i-1]
        nums.sort(reverse=True)
        count.sort(reverse=True)
        total = 0
        for num, count in zip(nums,count):
            total += (num * count)
        return total % (10**9 + 7)
        
        
        
\"\"\"
  1 2 3
0,1

\"\"\"
