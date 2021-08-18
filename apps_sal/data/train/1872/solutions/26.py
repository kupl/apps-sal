class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def check(root, level, d):
            if level not in d:
                d[level] = 0
            d[level] += root.val
            if root.left:
                check(root.left, level + 1, d)
            if root.right:
                check(root.right, level + 1, d)
            return

        d = dict()
        check(root, 1, d)
        rtv = 0
        maxs = -float('inf')
        for k in list(d.keys()):
            if d[k] > maxs:
                maxs = d[k]
                rtv = k
        return rtv
