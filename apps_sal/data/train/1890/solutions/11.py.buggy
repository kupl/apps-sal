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
         q = [root]
         lastRow = [root]
         # store = [[root]]
 
         while len(q) > 0:
             row = []
     
             while len(q) > 0:
                 popped = q[0]
                 q = q[1:]
             
                 if popped.left:
                     row.append(popped.left)
                 if popped.right:
                     row.append(popped.right)
             
             q = row
             if len(row) > 0:
                 # store.append(row)
                 lastRow = row
         return lastRow[0].val
         # return store[-1][0].val
 

