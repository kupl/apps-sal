class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count=1
        while k!=0:
            if missing_count not in arr:
                k-=1
                missing_count+=1
            else:
                missing_count+=1
        return missing_count-1

