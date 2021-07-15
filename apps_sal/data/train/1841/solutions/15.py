class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = sorted(arr)[(len(arr)-1)//2]
        return sorted(arr, key=lambda x:(abs(x-med),x), reverse=True)[:k]
