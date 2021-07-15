class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        nums = sorted(arr)
        median = nums[(len(nums) - 1) // 2]
        
        arr.sort(key = lambda x: ((abs(x - median)), x), reverse=True)
        
        res = []
        
        for num in arr:
            res.append(num)
            k -= 1
            if k == 0:
                break

        return res

