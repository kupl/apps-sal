# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def __init__(self):
         self.l=[]
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         if root == None:
             return []
         self.postorderTraversal(root.left)
         self.postorderTraversal(root.right)
         self.l.append(root.val)
         return self.l
