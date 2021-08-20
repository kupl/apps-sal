class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:

        def traverse(root, prev_min, prev_max):
            if root:
                prev_min = min(root.val, prev_min)
                prev_max = max(root.val, prev_max)
                return max(traverse(root.left, prev_min, prev_max), traverse(root.right, prev_min, prev_max))
            else:
                return prev_max - prev_min
        return traverse(root, root.val, root.val)
