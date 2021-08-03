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
         # nonlocal lowest
         lowest = {'depth':-1, 'horz':0, 'value':0}
         
         def check_and_update_lowest(depth, horz, value):
             if (depth > lowest['depth']) or (depth == lowest['depth'] and horz < lowest['horz']):
                 lowest['depth'] = depth
                 lowest['horz'] = horz
                 lowest['value'] = value
             
                 
         
         def deeper(node, level= 0, horz = 0):
             
             if node is None:
                 return
             
             if not(node.left or node.right):
                 check_and_update_lowest(level, horz, node.val)
                 return
             
             deeper(node.left,level+1, horz-1)
             deeper(node.right,level+1, horz+1)
             
         deeper(root)
         
         return lowest['value']
             
             
