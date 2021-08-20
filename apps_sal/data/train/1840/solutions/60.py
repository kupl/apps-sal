class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(node, direction, l):
            if not node:
                return
            self.ans = max(self.ans, l)
            helper((node.left, node.right)[direction], 1 - direction, l + 1)
            helper((node.left, node.right)[1 - direction], direction, 1)
        helper(root, 0, 0)
        helper(root, 1, 0)
        return self.ans
