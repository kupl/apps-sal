class Solution:

    def stoneGameII(self, piles: List[int]) -> int:

        def dfs(piles, l, m):
            if (l, m) in self.mem:
                return self.mem[l, m]
            ret = 0
            r = min(len(piles), l + 2 * m)
            for i in range(l + 1, r + 1):
                other = dfs(piles, i, max(m, i - l))
                cur = sum(piles[l:]) - other
                ret = max(ret, cur)
            self.mem[l, m] = ret
            return ret
        self.mem = dict()
        return dfs(piles, 0, 1)
    '\n    def stoneGameII(self, piles: List[int]) -> int:\n        def dfs(piles, m):\n            ret = 0\n            r = min(len(piles), 2*m)\n            for i in range(1, r+1):\n                other = dfs(piles[i:], max(m, i))\n                cur = sum(piles) - other\n                ret = max(ret, cur)\n            return ret\n        \n        ans = dfs(piles, 1)\n        return ans\n    '
