# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, m = -10**4) -> int:
        
        return (self.goodNodes(root.left, max(m, root.val))+self.goodNodes(root.right, max(m, root.val))+(root.val>=m)) if root else 0
    
           
        

