class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0

        def preorder(root, minval, maxval):
            if not root:
                self.ans = max(self.ans, abs(minval - maxval))
                return
            (minval, maxval) = (min(minval, root.val), max(maxval, root.val))
            preorder(root.left, minval, maxval)
            preorder(root.right, minval, maxval)
        preorder(root, float('inf'), float('-inf'))
        return self.ans
