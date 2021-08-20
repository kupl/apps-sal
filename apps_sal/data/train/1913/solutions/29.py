class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        prev_vals = [(float('inf'), None)]
        for i in range(len(A) - 1, -1, -1):
            num = A[i]
            if num > prev_vals[-1][0]:
                max_prev = 0
                ind = None
                while num > prev_vals[-1][0]:
                    (prev_n, prev_ind) = prev_vals.pop()
                    if prev_n > max_prev:
                        max_prev = prev_n
                        ind = prev_ind
                (A[i], A[ind]) = (max_prev, num)
                return A
            prev_vals.append((num, i))
        return A
