# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def helper(root, max_sofar):
            
            if not root:
                return 0
            
            total = 0
            if root.val >= max_sofar:
                total += 1
                
            total += helper(root.left, max(max_sofar, root.val))
            total += helper(root.right, max(max_sofar, root.val))
            
            return total
        
        return helper(root, float(\"-inf\"))
