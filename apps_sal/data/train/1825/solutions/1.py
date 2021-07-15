# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def traverse(node):
            if not node:
                return 0, None
            hl, lcal = traverse(node.left)
            hr, lcar = traverse(node.right)
            if hl < hr:
                return hr + 1, lcar
            elif hl > hr:
                return hl + 1, lcal
            else:
                return hl + 1, node
            
        return traverse(root)[1]
        
        
        
        
                
        
    
    
    
    
    
    
    
    
    
    

