class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A = sorted(A)
        min1 = set()
        max1 = set()
        for i in range(K + 1):
            min1.add(A[0] + i)

        for i in range(K, -1, -1):
            max1.add(A[-1] - i)

        # print(min1,max1)

        s1 = min1 & max1
        if len(s1) > 0:
            return 0
        else:
            return min(list(max1)) - max(list(min1))
