# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         def inorder(root):
             if root:
                 yield from inorder(root.left)
                 yield root.val
                 yield from inorder(root.right)
         
         it = inorder(root)
         
         prev = next(it)
         m_ = 1 << 31
         
         while True:
             n = next(it, False)
             if not n:
                 break
             m_ = min(m_, abs(n - prev))
             prev = n
   
         return m_        
