# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dist = 0

        def dfs(node, ancesVal):
            # print(ancesVal)
            if not node:
                self.dist = max(self.dist, abs(max(ancesVal) - min(ancesVal)))
                return

            dfs(node.left, ancesVal + [node.val])

            dfs(node.right, ancesVal + [node.val])
            return

        dfs(root, [])
        return self.dist
