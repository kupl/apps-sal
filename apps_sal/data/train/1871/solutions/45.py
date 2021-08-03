# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxval = float('-inf')

        def dfs(node, ans):
            if node:
                if ans:
                    self.maxval = max(self.maxval, abs(max(ans) - node.val))
                    self.maxval = max(self.maxval, abs(min(ans) - node.val))

                dfs(node.left, ans + [node.val])
                dfs(node.right, ans + [node.val])
        dfs(root, [])
        return self.maxval
