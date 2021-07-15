# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if not root:
             return []
         
         cur_level,levelOrder,level=[root],[],1
         while cur_level:
             next_level,vals=[],[]
             for node in cur_level:
                 vals.append(node.val)
                 if node.left:
                     next_level.append(node.left)
                 if node.right:
                     next_level.append(node.right)
             if level%2==1:
                 levelOrder.append(vals)
             else:
                 levelOrder.append(vals[::-1])
             level+=1
             cur_level=next_level
         return levelOrder
