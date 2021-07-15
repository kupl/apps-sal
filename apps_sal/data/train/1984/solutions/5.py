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
         INDICES = {}
         for idx, val in enumerate(inorder):
             INDICES[val] = idx
             
         ptr = 0
         def build(left, right):
             nonlocal ptr
             if left > right or right < left or ptr >= len(preorder):
                 return 
             val = preorder[ptr]
 
             node = TreeNode(preorder[ptr])
             ptr += 1
             node.left = build(left, INDICES[val]-1) 
             node.right = build(INDICES[val]+1, right) 
             
             return node
         
         return build(0, len(inorder))
             
