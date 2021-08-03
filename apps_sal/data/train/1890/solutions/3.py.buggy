# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findBottomLeftValue(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         last = [root]
         now = []
         for node in last:
             if node.left:
                 now.append(node.left)
             if node.right:
                 now.append(node.right)
         
         while now:
             last, now = now, []
             for node in last:
                 if node.left:
                     now.append(node.left)
                 if node.right:
                     now.append(node.right)   
         
         return last[0].val
