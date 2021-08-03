class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        already_sorted = True
        swap_left = None
        for i in range(len(A) - 1, 0, -1):
            if A[i] < A[i - 1]:
                swap_left = (i - 1, A[i - 1])
                already_sorted = False
                break
        if already_sorted:
            return A
        swap_right = None
        for i in range(swap_left[0] + 1, len(A)):
            if A[i] < swap_left[1]:
                if swap_right and A[i] <= swap_right[1]:
                    continue
                else:
                    swap_right = (i, A[i])
        A[swap_right[0]], A[swap_left[0]] = swap_left[1], swap_right[1]
        return A
