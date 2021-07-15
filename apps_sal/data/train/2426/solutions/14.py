class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        M, m = max(A), min(A)
        if M-m <= 2*K:
            return 0
        else:
            return (M-K)-(m+K)
