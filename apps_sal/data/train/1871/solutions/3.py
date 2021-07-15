# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        
        self.max_diff = -float(\"inf\")
        
        
        def helper(root, ancestors):
            if root is None:
                return
            
            for ancestor in ancestors:
                if abs(root.val - ancestor) > self.max_diff:
                    self.max_diff = abs(root.val - ancestor)
            
            helper(root.left, ancestors + [root.val])
            helper(root.right, ancestors + [root.val])
        
        helper(root, [root.val])
        
        return self.max_diff
