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
         if root is None:
             return []
         r = []
         s = [root]
         t = []
         while True:
             mx = float('-inf')
             for x in s:
                 if x.left != None:
                     t.append(x.left)
                 if x.right != None:
                     t.append(x.right)
                 if x.val > mx:
                     mx = x.val
             r.append(mx)
             if len(t)>0:
                 s=t
                 t=[]
             else:
                 return r
