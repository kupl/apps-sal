class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        if K == 0:
            return max(A) - min(A)
        if len(set(A)) == 1:
            return 0
        mean = (max(A) + min(A)) // 2
        B = []
        for num in A:
            if num + K < mean:
                B.append(num + K)
            elif num - K > mean:
                B.append(num - K)
            else:
                B.append(mean)
        return max(B) - min(B)
