class Solution:

    def specialArray(self, a: List[int]) -> int:
        (n, i) = (len(a), 0)
        a.sort(reverse=True)
        (l, r) = (0, n)
        while l < r:
            m = l + (r - l) // 2
            if m < a[m]:
                l = m + 1
            else:
                r = m
        return -1 if l < n and l == a[l] else l
