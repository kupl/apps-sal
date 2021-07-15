# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        def Search(root,left,height):
            if root is None:
                return height
            if left:
                return max(Search(root.left,1,0),Search(root.right,0,height+1))
            else:
                return max(Search(root.right,0,0),Search(root.left,1,height+1))
        return max(Search(root.left,1,0),Search(root.right,0,0))
        
        
        
        

