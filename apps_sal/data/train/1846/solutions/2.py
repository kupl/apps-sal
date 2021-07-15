# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def prune(node: TreeNode) -> bool:
            
            
            if not node:
                return True
            
            # if node is 1, the tree with node as root does not need to be pruned

            
            left_prune = prune(node.left)
            right_prune = prune(node.right)
            
            if prune(node.left):
                node.left = None
            if prune(node.right):
                node.right = None
            
            return (node.val == 0) and left_prune and right_prune
        
        
        
        if prune(root):
            return None
        
        return root

