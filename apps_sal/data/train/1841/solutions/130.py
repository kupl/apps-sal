class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return []
        elif len(arr) <= k:
            return arr
        arr.sort()
        n = len(arr)
        median = arr[int((n-1)/2)]
        arr = [(abs(i-median), i) for i in arr]
        arr.sort(reverse=True)
        return [i[1] for i in arr[:k]]

