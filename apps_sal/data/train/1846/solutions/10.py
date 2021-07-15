# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left_sub = self.pruneTree(root.left)
        right_sub = self.pruneTree(root.right)
        if root.val  == 0 and left_sub == None and right_sub == None:
            return None
        root.left  = left_sub
        root.right = right_sub
        return root
        

