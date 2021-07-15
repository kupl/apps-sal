class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        arr.sort(reverse=True)
        m=arr[ceil((n-1)/2)]
        arr.sort(key=lambda x: abs(x-m), reverse=True)
        return arr[:k]
