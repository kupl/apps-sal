# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         trav = []
         self.post(root, trav)
         return trav
     
     def post(self, node, trav):
         if not node: return
         self.post(node.left, trav)
         self.post(node.right, trav)
         trav.append(node.val)
         
