class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        def flip(idx):
            arr[:idx+1] = arr[:idx+1][::-1]
        for i in range(len(arr)):
            maxInd = arr[:n].index(max(arr[:n]))
            if maxInd != n:
                ans.append(maxInd+1)
                ans.append(n)
                flip(maxInd)
                flip(n -1)
            n -= 1
        
        return ans

