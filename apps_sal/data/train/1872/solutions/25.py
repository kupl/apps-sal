class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d = {}

        def f(root, level):
            if root:
                if level in d:
                    d[level] += root.val
                else:
                    d[level] = root.val
                f(root.left, level + 1)
                f(root.right, level + 1)

        f(root, 1)
        m = max(d.values())
        for k in d:
            if d[k] == m:
                return k
