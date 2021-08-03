class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        A.sort(reverse=True)

        while len(A) > 2:
            max_num = A.pop(0)
            if max_num >= A[0] + A[1]:
                continue
            else:
                return max_num + A[0] + A[1]
        return 0
