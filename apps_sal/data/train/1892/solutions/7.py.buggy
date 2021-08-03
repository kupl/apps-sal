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
         _, res = self.recPathSum(root, sum)
         return res
     
     def recPathSum(self, root, sum):
         if not root:
             return (False, [])
         if root.val == sum:
             if not root.left and not root.right:
                 return (True, [[root.val]])
         foundLeft, listLeft = self.recPathSum(root.left, sum - root.val)
         foundRight, listRight = self.recPathSum(root.right, sum - root.val)
         res = []
         if foundLeft:
             res = [[root.val] + l for l in listLeft]
         if foundRight:
             res += [[root.val] + l for l in listRight]
         return (foundLeft or foundRight, res)
