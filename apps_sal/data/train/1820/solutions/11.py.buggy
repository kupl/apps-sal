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
         if root==None:
             return []
         if root.left==None and root.right==None:
             return [root.val]
         if root.left:
             l = self.largestValues(root.left)
         else:
             l = []
         if root.right:
             r = self.largestValues(root.right)
         else:
             r = []
         out = [root.val]
         for i in range(min(len(l),len(r))):
             out.append(max(l[i],r[i]))
         if len(l)<len(r):
             out = out + r[len(l):]
         elif len(r)<len(l):
             out = out + l[len(r):]
         return out
         
