class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pts = []
        for start, end in requests:
            pts.append((start, 1))
            pts.append((end + 1, -1))  # open bracket

        pts.sort(key=lambda x: (x[0], x[1]))

        N = len(nums)
        cnts = []
        # 2 pointers
        j = 0
        cur = 0
        for i in range(N):
            if j == len(pts):
                cnts.append(cur)
                continue
            if pts[j][0] > i:
                cnts.append(cur)
            elif pts[j][0] == i:
                while j < len(pts) and pts[j][0] == i:
                    cur += pts[j][1]
                    j += 1
                cnts.append(cur)
        cnts.sort()
        nums.sort()
        ans = 0
        MOD = 10 ** 9 + 7
        for c, n in zip(cnts, nums):
            ans += c * n
            ans %= MOD
        return ans

        N = len(nums)
        tree = [0] * (4 * N)
        lazy = [0] * (4 * N)
        arr = nums

        def _push_down(rt, diff):
            lazy[rt * 2 + 1] += diff
            lazy[rt * 2 + 2] += diff

        def update_range_by_one(rt, lo, hi, i, j):
            if j < lo or i > hi:
                return
            if lazy[rt] != 0:
                tree[rt] += (hi - lo + 1) * lazy[rt]
                if lo != hi:
                    _push_down(rt, lazy[rt])
                lazy[rt] = 0
            if lo >= i and hi <= j:
                tree[rt] += (hi - lo + 1)
                if lo != hi:
                    _push_down(rt, 1)
                return
            mid = (lo + hi) // 2
            update_range_by_one(rt * 2 + 1, lo, mid, i, j)
            update_range_by_one(rt * 2 + 2, mid + 1, hi, i, j)
            tree[rt] = tree[2 * rt + 1] + tree[2 * rt + 2]

        def query(rt, lo, hi, i):
            if lazy[rt] != 0:
                tree[rt] += (hi - lo + 1) * lazy[rt]
                if lo != hi:
                    _push_down(rt, lazy[rt])
                lazy[rt] = 0
            if lo == hi == i:
                return tree[rt]
            mid = (lo + hi) // 2
            if i <= mid:
                return query(rt * 2 + 1, lo, mid, i)
            else:
                return query(rt * 2 + 2, mid + 1, hi, i)

        MOD = 10 ** 9 + 7
        for i, j in requests:
            update_range_by_one(0, 0, N - 1, i, j)

        cnts = []
        for i in range(N):
            cnts.append(query(0, 0, N - 1, i))
        cnts.sort()
        nums.sort()

        ans = 0
        for c, n in zip(cnts, nums):
            ans += c * n
            ans %= MOD
        return ans
