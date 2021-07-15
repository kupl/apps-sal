# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0
    
    def dfs(self, root):
        if not root:
            return (0, 0)        
        if not root.left and not root.right:
            return (root.val, root.val)        
        left_min = right_min = float('inf')
        left_max = right_max = float('-inf')
        if root.left:
            left_min, left_max = self.dfs(root.left)        
        if root.right:
            right_min, right_max = self.dfs(root.right)
        min_val = min(left_min, right_min)
        max_val = max(left_max, right_max)        
        self.res = max(self.res, abs(root.val - min_val), abs(root.val - max_val))
        return (min(min_val, root.val), max(max_val, root.val))
    
    def maxAncestorDiff(self, root):
        \"\"\"
        :type root: TreeNode
        :rtype: int
        \"\"\"
        self.dfs(root)        
        return self.res
    
