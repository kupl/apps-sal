# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def lca(root=root):
            if root:
                n1, d1 = lca(root.left)
                n2, d2 = lca(root.right)
                if d1 == d2:
                    return (root, d1 + 1)
                else:
                    return (n1, 1 + d1) if d1 > d2 else (n2, 1 + d2)
            return (None, -1)
        
        return lca()[0]
                        
                        
                
                

