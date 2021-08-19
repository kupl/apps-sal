# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxDiff = 0

        def dfs(node):
            if not node:
                return []

            vals = dfs(node.left)
            vals.extend(dfs(node.right))

            nonlocal maxDiff
            localMaxDiff = max([abs(v - node.val) for v in vals]) if vals else 0
            maxDiff = max(maxDiff, localMaxDiff)
            vals.append(node.val)
            return vals

        dfs(root)
        return maxDiff
