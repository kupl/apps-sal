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
         def build(stop):
             if preorder and inorder[-1] != stop:
                 root = TreeNode(preorder.pop())
                 root.left = build(root.val)
                 inorder.pop()
                 root.right = build(stop)
                 return root
             return None # can be skipped
         
         preorder.reverse()
         inorder.reverse()
         return build(None)
