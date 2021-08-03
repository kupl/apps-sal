class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return A

        prev = A[0]
        swapping = (0, -1)
        to_swap = (0, -1)
        for ind in range(1, len(A)):
            num = A[ind]
            if num < prev:
                swapping = (num, ind)
                to_swap = (A[ind - 1], ind - 1)
            elif num > swapping[0] and num < to_swap[0]:
                swapping = (num, ind)

            prev = num

        if swapping[1] != -1:
            value = A[swapping[1]]
            A[swapping[1]] = A[to_swap[1]]
            A[to_swap[1]] = value

        return A
