# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.result = []
         
         def insert_node(node):
             if node:
                 self.result.append(node.val)
                 insert_node(node.left)
                 insert_node(node.right)
             else:
                 return
         insert_node(root)
         
         self.result.sort()
         
         minimum = None
         
         for i in range(len(self.result) - 1):
             diff = self.result[i + 1] - self.result[i]
             if not minimum:
                 minimum = diff
             elif minimum > diff:
                 minimum = diff
             if minimum == 0:
                 return minimum
         return minimum
             
         
         
