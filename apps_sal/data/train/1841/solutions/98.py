class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        a = arr
        a.sort()
        n = len(a)
        m = a[n - 1 >> 1]
        ans = []
        (l, h) = (0, n - 1)
        while len(ans) < k:
            if abs(a[l] - m) > abs(a[h] - m):
                ans.append(a[l])
                l += 1
            elif abs(a[l] - m) < abs(a[h] - m):
                ans.append(a[h])
                h -= 1
            elif a[l] >= a[h]:
                ans.append(a[l])
                l += 1
            else:
                ans.append(a[h])
                h -= 1
        return ans
