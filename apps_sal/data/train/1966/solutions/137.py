class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:

        def counts(nums):
            endhere = [0] * len(nums)
            st = []
            for (i, num) in enumerate(nums):
                while st and nums[st[-1]] >= num:
                    st.pop()
                if not st:
                    endhere[i] = num * (i + 1)
                else:
                    prev_idx = st[-1]
                    endhere[i] = endhere[prev_idx]
                    endhere[i] += num * (i - prev_idx)
                st.append(i)
            return sum(endhere)
        rows = mat[0][:]
        ans = counts(rows[:])
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[j] += 1
                else:
                    rows[j] = 0
            ans += counts(rows[:])
        return ans
