class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        longest = 0
        if not root:
            return longest

        def helper(root, level, direction):
            nonlocal longest
            if level > longest:
                longest = level
            if direction:
                if root.left:
                    helper(root.left, level + 1, not direction)
                if root.right:
                    helper(root.right, 1, direction)
            else:
                if root.right:
                    helper(root.right, level + 1, not direction)
                if root.left:
                    helper(root.left, 1, direction)
        if root.right:
            helper(root.right, 1, True)
        if root.left:
            helper(root.left, 1, False)
        if not root.left and (not root.right):
            return 0
        return longest
