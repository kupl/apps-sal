class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        nums = set()
        for number in arr2:
            for n in range(number-d, number+d+1):
                nums.add(n)
            
        cnt = 0
        for number in arr1:
            if number not in nums:
                cnt += 1
        
        return cnt
