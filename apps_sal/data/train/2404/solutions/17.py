class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        if len(a) == a[-1]:
            return a[-1]+k
        # print(list(range(a[0],a[-1]+1)))
        # print([x for x in range(1,a[-1]+1) if x not in a])
        t = [x for x in range(1,a[-1]+1) if x not in a]
        if len(t) < k:
            return a[-1] +k-len(t)
        else:
            return t[k-1]

