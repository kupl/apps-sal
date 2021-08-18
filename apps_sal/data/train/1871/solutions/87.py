class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_p_diff = 0

        def max_diff(node, p_min, p_max):
            if not node:
                return
            self.max_p_diff = max(self.max_p_diff, max(abs(node.val - p_min), abs(p_max - node.val)))
            p_min = min(node.val, p_min)
            p_max = max(node.val, p_max)
            max_diff(node.left, p_min, p_max)
            max_diff(node.right, p_min, p_max)
        max_diff(root, root.val, root.val)
        return self.max_p_diff
