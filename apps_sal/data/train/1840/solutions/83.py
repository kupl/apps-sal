# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        return self.dfs(root)[-1]
    
    def dfs(self, root):
        if not root:
            return [-1, -1, -1] # left, right, total
        
        left, right = self.dfs(root.left), self.dfs(root.right)
        
        return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[-1], right[-1])]
