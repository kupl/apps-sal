# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         if not root:
             return []
         
         res = []
         
         stack = [ (root, root.val, [root.val]) ]
         
         while stack:
             curr, currsum, currp = stack.pop()
             if not curr.left and not curr.right:
                 if currsum == sum:
                     res.append( currp )
             for child in [curr.left, curr.right]:
                 if child:
                     stack.append( (child, currsum + child.val, currp + [child.val]) )
         
         return res
         
