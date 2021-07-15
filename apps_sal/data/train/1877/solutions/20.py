# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        \"\"\"
        return the root so that every node is a sufficient
        Approach:
        1. For any given node, if all of its children have a path sum < than limit, or None, delete the node
        2. Post-order traversal, at the leaf node, if the path sum < than limit, delete node, then work your way up
        \"\"\" 
        
        leaf = True
        # check left child alive
        if root.left is not None:
            root.left = self.sufficientSubset(root.left, limit - root.val)
            leaf = False
            
        # check right child alive
        if root.right is not None:
            root.right = self.sufficientSubset(root.right, limit - root.val)   
            leaf = False
            
        # if the node is not leaf and left and right are not alive -> set to null
\t\t# if the node is leaf but less than limit -> set to null
        if root.left is None and root.right is None and ( root.val < limit or not leaf):
            root = None

        return root
                
                
                
            
                
