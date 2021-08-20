class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        candidates = []

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                l and candidates.append(l)
                r and candidates.append(r)
            return 1 + l + r
        dfs(root)
        candidates.append(n - (1 + sum(candidates)))
        return any((mine > n - mine for mine in candidates))
