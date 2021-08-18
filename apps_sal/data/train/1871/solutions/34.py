class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        paths = []

        def pathsToLeafs(root, comp):
            if not root:
                return
            if not root.left and not root.right:
                paths.append(comp + [root.val])
                return
            pathsToLeafs(root.left, comp + [root.val])
            pathsToLeafs(root.right, comp + [root.val])
        pathsToLeafs(root, [])

        def maxDiff(a):
            val = 0
            n = len(a)
            dp = [0] * n
            for i in range(1, n):
                val = max(val + a[i] - a[i - 1], dp[i])
                dp[i] = max(val, dp[i - 1])
            return dp[-1]

        res = 0
        for path in paths:
            print(path)
            res = max(res, maxDiff(path), maxDiff(path[::-1]))
        return res
