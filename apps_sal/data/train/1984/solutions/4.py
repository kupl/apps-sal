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
         if not preorder or not inorder:
             return None
         root = TreeNode(preorder.pop(0))
         index = inorder.index(root.val)
         root.left = self.buildTree(preorder, inorder[:index])
         root.right = self.buildTree(preorder, inorder[index+1:])
         return root
 
 class Solution:
     # @param inorder, a list of integers
     # @param postorder, a list of integers
     # @return a tree node
     # 12:00
     def buildTree(self, preorder, inorder):
         dicinorder = {}
         for i,val in enumerate(inorder):
             dicinorder[val] = i
         start, end = 0, len(inorder)
         return self.helper(start, end, preorder, dicinorder)
     
     def helper(self, start, end, preorder, dicinorder):
         if start == end:
             return None
         root = TreeNode(preorder.pop(0))
         inorderIndex = dicinorder[root.val]
         root.left = self.helper(start, inorderIndex, preorder, dicinorder)
         root.right = self.helper(inorderIndex+1, end, preorder, dicinorder)
         return root
