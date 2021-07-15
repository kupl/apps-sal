# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def largestValues(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         result=[]
         if root==None:
             return result
         queue=[root]
         curr_row_values=[]
         next_queue=[]
         while len(queue)>0:
             node=queue.pop()
             
             if node!=None:
                 curr_row_values.append(node.val)
                 next_queue.append(node.left)
                 next_queue.append(node.right)
             if len(queue)==0 and len(next_queue)>0:
                 result.append(max(curr_row_values))
                 curr_row_values=[]
                 queue=next_queue
                 next_queue=[]
         return result
