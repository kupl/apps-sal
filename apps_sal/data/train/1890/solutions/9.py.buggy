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
         queue = [root]
         i = 0
         while i < len(queue):
             queue += filter(lambda node: bool(node), [queue[i].right, queue[i].left])
             i += 1
 
         return queue[-1].val
