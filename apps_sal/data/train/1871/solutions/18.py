class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:

        def mdiff(root, maxval, minval):
            if not root:
                return -1
            maxval = max(root.val, maxval)
            minval = min(minval, root.val)
            return max(abs(maxval - minval), mdiff(root.left, maxval, minval), mdiff(root.right, maxval, minval))
        return mdiff(root, 0, 100000)
