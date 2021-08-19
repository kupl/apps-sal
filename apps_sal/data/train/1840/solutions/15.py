class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def ZigZag(node):
            if not node:
                return [-1, -1, -1]
            left = ZigZag(node.left)
            right = ZigZag(node.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
        return ZigZag(root)[-1]
