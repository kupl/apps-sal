# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0
        memo = {}

        def dfs2(node, direction):
            if not node:
                return 0

            if (node, direction) not in memo:
                if direction == False:
                    memo[(node, direction)] = 1 + dfs2(node.right, True)
                else:
                    memo[(node, direction)] = 1 + dfs2(node.left, False)

            return memo[(node, direction)]

        def dfs1(node):
            if not node:
                return

            self.ans = max(self.ans, dfs2(node, True) - 1, dfs2(node, False) - 1)

            dfs1(node.left)
            dfs1(node.right)

        dfs1(root)
        return self.ans
