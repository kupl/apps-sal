# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findFrequentTreeSum(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         res = dict()
         def helper(root):
             if not root:
                 return 0
             val = root.val + helper(root.left) + helper(root.right)
             if val in res:
                 res[val] += 1
             else:
                 res[val] = 1
             return val
             
         helper(root)
         if not res:
             return []
         
         max_val = max(res.values())
         return [k for k, v in res.items() if v == max_val]
