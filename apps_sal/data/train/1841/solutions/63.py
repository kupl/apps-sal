class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        ans = []
        lo, hi = 0, n - 1
        while lo <= hi and k > 0:
            dlo, dhi = abs(arr[lo] - m), abs(arr[hi] - m)
            if dlo > dhi:
                ans.append(arr[lo])
                lo += 1
            else:
                ans.append(arr[hi])
                hi -= 1
            k -= 1
        return ans
