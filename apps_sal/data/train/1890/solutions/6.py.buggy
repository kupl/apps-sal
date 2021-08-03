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
         queue=[root]
         
         while queue:
             new_queue=[]
             for node in queue:
                 if node.left:
                     new_queue.append(node.left)
                 if node.right:
                     new_queue.append(node.right)
             if new_queue==[]:
                 return queue[0].val
             queue=new_queue
