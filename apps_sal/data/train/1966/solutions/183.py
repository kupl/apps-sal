class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def helper(h):
            res = 0
            st = []
            sum_ = [0] * len(h)
            for i in range(len(h)):
                while len(st) > 0 and h[st[-1]] >= h[i]:
                    st.pop()

                if len(st) > 0:
                    left_bound = st[-1]
                    sum_[i] += sum_[left_bound]
                    sum_[i] += h[i] * (i - left_bound)
                else:
                    sum_[i] = h[i] * (i + 1)

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
