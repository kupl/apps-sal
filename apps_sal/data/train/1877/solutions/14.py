# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def remove(node, val):
            if not node: return val
            l = remove(node.left, node.val+val)
            r = remove(node.right, node.val+val)
            
            
            result = 0
            if node.left and node.right:
                result = max(l,r)
            elif node.left:
                result = l
            else: #node.right = None or both left right are None
                result = r
            
            if l<limit:
                node.left = None
            if r<limit:
                node.right = None
            
            return result
            
        val = remove(root,0)
        
        return None if val < limit else root

