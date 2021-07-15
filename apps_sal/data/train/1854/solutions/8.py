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
         # if not root:
         #     return 0
         # res = 0
         # if root.left:
         #     if root.left.left:
         #         res += self.rob(root.left.left)
         #     if root.left.right:
         #         res += self.rob(root.left.right)
         # if root.right:
         #     if root.right.left:
         #         res += self.rob(root.right.left)
         #     if root.right.right:
         #         res += self.rob(root.right.right)
         # return max(res + root.val, self.rob(root.left) + self.rob(root.right))
         
         print(self.helper(root))
         return max(self.helper(root))
         
     def helper(self, root):
         if not root:
             return [0,0]
         left = self.helper(root.left)
         right = self.helper(root.right)
         res = [0, 0] # index = 0 not rob, index 1 rob
         res[0] = max(left) + max(right)
         res[1] = left[0] + right[0] + root.val
         return res
         
              
             
             
         
