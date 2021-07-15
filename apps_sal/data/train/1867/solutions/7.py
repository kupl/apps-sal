# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def getlist(self, root):
         if root == None:
             return []
         
         s = []
         
         if root.left != None:
             s = s + self.getlist(root.left)
         s = s + [root.val]
         if root.right != None:
             s = s + self.getlist(root.right)
         return s
             
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         s = self.getlist(root)
         if len(s) == 0:
             return 0
         return s[k - 1]
         
                 
             
