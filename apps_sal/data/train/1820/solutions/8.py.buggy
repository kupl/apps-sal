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
         if not root:
             return []
         
         queue = [root]
         ans = []
         
         while queue:
             temp = -float("inf")
             size = len(queue)            
             for i in range(size):
                 node = queue.pop(0)
                 temp = max(temp, node.val)
                 if node.left:
                     queue.append(node.left)
                 if node.right:
                     queue.append(node.right)
             ans.append(temp)
             
         return ans
                 
         
