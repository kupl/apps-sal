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
         null = TreeNode(None)
         max_idx = len(preorder)
         lookups = {}
         
         def _build(parent, p, i):
             print(parent.val, p, i) #REM
             if p >= max_idx:
                 return
             
             node = TreeNode(preorder[p])
             parent.left = node
             print('.. left', node.val) #REM
             lookups[node.val] = node
             
             while p < max_idx and preorder[p] == inorder[i]:
                 
                 while i < max_idx and inorder[i] in lookups:
                     node = lookups[inorder[i]]
                     i += 1
 
                 p += 1
                 
                 if p < max_idx:
                     right = TreeNode(preorder[p])
                     lookups[right.val] = right
                     print('.. right of', node.val, ' -> ', right.val) #REM
                     node.right = right
                     node = right
 
             _build(node, p + 1, i)
         
         _build(null, 0, 0)
         
         return null.left

