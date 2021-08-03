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
         preindex = [0]
         ind = {v:i for i, v in enumerate(inorder)}
         head = self.buildTreeCore(0, len(preorder) - 1, preorder, inorder, ind, preindex)
         return head
     
     def buildTreeCore(self, start, end, preorder, inorder, ind,preindex):
         if start <= end:
             mid = ind[preorder[preindex[0]]]
             preindex[0] =preindex[0]+1
             root = TreeNode(inorder[mid])
             root.left = self.buildTreeCore(start, mid - 1, preorder, inorder, ind, preindex)
             root.right = self.buildTreeCore(mid + 1, end, preorder, inorder, ind, preindex)
             return root
