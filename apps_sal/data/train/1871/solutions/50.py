# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_diff = -float('inf')
        
        def helper(node, vals):
            
            if not node:
                self.max_diff = max(self.max_diff,abs(max(vals)-min(vals)))
                return 
            
            helper(node.left,vals + [node.val])
            helper(node.right,vals + [node.val])
                
        helper(root, [root.val])
        
        return self.max_diff
                

