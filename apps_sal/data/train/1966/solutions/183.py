class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack
        # similar idea: 84. Largest Rectangle in Histogram
        # process row by row
        def helper(h):  # h is the effective cummulative height at position j
            res = 0
            st = []
            # store number of rectangle (all ones) with h[i] as bottom-right corner
            sum_ = [0] * len(h)
            for i in range(len(h)):
                # pop those higher blocks, since it will not give more rectangles
                while len(st) > 0 and h[st[-1]] >= h[i]:
                    st.pop()

                # if we have a lower block in the stack
                if len(st) > 0:
                    left_bound = st[-1]
                    # Extend the previous rectangular at index \"left_bound\".
                    # every rectangle that has left_bound as bottom-right corner can be extended to current index
                    # thus sum_[i] += sum_[left_bound]
                    # add rectangles that have height same as h[left_bound]
                    sum_[i] += sum_[left_bound]
                    sum_[i] += h[i] * (i - left_bound)  # add rectangles with height h[i]
                    ## width =  (i - left_bound)
                else:
                    sum_[i] = h[i] * (i + 1)  # left_bound = -1

                st.append(i)

            return sum(sum_)

        res = 0
        h = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    h[j] += 1
                else:
                    h[j] = 0

            res += helper(h)
        return res
