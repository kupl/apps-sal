# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
   def buildTree(self, preorder, inorder):
     """
     :type preorder: List[int]
     :type inorder: List[int]
     :rtype: TreeNode
     """
     lookup = {}
     for i,num in enumerate(inorder):
         lookup[num] = i 
         
     return self.buildrecurtree(lookup, preorder,inorder, 0,0,len(inorder))
 
   def buildrecurtree(self, lookup, preorder, inorder, pre_start, in_start, in_end):
     if (in_start == in_end):
         return None
     node = TreeNode(preorder[pre_start])
     i = lookup[preorder[pre_start]]
     node.left = self.buildrecurtree(lookup, preorder, inorder, pre_start + 1, in_start, i)
     node.right = self.buildrecurtree(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
     return node
         
