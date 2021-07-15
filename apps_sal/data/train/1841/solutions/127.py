class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        m = (n-1) // 2
        arr.sort()
        
        median = arr[m]
        print(median)
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        return arr[:k]
