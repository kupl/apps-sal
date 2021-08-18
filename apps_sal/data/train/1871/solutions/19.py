class Solution:
    def maxAncestorDiff(self, node: TreeNode) -> int:
        def helper(node, max_val, min_val):
            if not node:
                return 0

            diff = max(abs(max_val - node.val), abs(min_val - node.val))
            max_val = max(node.val, max_val)
            min_val = min(node.val, min_val)
            return max(helper(node.left, max_val, min_val), helper(node.right, max_val, min_val), diff)

        if not node:
            return 0

        return helper(node, node.val, node.val)
