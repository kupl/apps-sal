class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=max(arr)
        a=[]
        for i in range(1,m+k+1):
            if i not in arr:
                a.append(i)
        a=sorted(a)
        return a[k-1]
