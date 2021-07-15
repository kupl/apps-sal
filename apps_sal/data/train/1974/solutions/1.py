# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         ans = []
         if (root == None): return ans
         self.helper(root,ans)
         return ans
     
     def helper(self,root,ans):
         if (root == None):
             return
         self.helper(root.left,ans)
         self.helper(root.right,ans)
         ans.append(root.val)
