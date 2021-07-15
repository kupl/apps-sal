class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k: return k
        counts = arr[0]-1
        for i in range(1, len(arr)):
            gap = arr[i]-arr[i-1]-1
            if gap == 0: continue
            if counts+gap >= k: return arr[i-1]+k-counts
            else: counts += gap
        return arr[-1]+k-counts
            
            

