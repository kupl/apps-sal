class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        if not A or not B:
            return ans

        cur_a = A.pop(0)
        cur_b = B.pop(0)

        while cur_a and cur_b:
            if cur_a[0] <= cur_b[1] and cur_a[1] >= cur_b[0]:
                ans.append([max(cur_a[0], cur_b[0]), min(cur_a[1], cur_b[1])])

            old_a = cur_a
            if cur_a[1] <= cur_b[1]:
                cur_a = A.pop(0) if A else None
            if old_a[1] >= cur_b[1]:
                cur_b = B.pop(0) if B else None

        return ans
