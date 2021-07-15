# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         yield_value = {}
         
         def helper(node, can_rob):
             if not node:
                 return 0
             
             if (node.left, True) not in yield_value:
                 left_yield_t = helper(node.left, True)
                 yield_value[(node.left, True)] = left_yield_t
             if (node.right, True) not in yield_value:
                 right_yield_t = helper(node.right, True)
                 yield_value[(node.right, True)] = right_yield_t            
             if (node.left, False) not in yield_value:
                 left_yield_f = helper(node.left, False)
                 yield_value[(node.left, False)] = left_yield_f
             if (node.right, False) not in yield_value:
                 right_yield_f = helper(node.right, False)
                 yield_value[(node.right, False)] = right_yield_f
                 
             if not can_rob:
                 return yield_value[(node.left, True)] + yield_value[(node.right, True)]
             
             else:
                 return max(
                     (node.val + yield_value[(node.left, False)] + yield_value[(node.right, False)]), 
                     (yield_value[(node.left, True)] + yield_value[(node.right, True)] )
                 )
         
         return helper(root, True)
