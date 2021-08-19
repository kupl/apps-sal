class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0

        def helper(node, max_val, min_val):
            if not node:
                self.res = max(self.res, max_val - min_val)
                return
            helper(node.left, max(max_val, node.val), min(min_val, node.val))
            helper(node.right, max(max_val, node.val), min(min_val, node.val))
        helper(root, 0, 100000)
        return self.res
