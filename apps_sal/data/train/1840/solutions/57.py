class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0

        def helper(root, direction):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left, 'left')
            right = helper(root.right, 'right')
            res = max(res, left + 1, right + 1)
            return right + 1 if direction == 'left' else left + 1
        if not root:
            return 0
        helper(root, 'left')
        helper(root, 'right')
        return res - 1
