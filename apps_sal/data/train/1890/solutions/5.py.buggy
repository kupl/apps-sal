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
         q = [(root,1)]
         cur = (root,1)
         while (q!=[]):
             node,depth = q.pop(0)
             if depth > cur[1]:
                 cur = (node,depth)
             if node.left != None:
                 q.append((node.left,depth + 1))
             if node.right != None:
                 q.append((node.right,depth + 1))
         return cur[0].val
