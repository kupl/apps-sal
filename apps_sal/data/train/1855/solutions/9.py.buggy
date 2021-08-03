# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:   
     
     def valid(self, me, parents_lt, parents_gt):
         if me is None:
             return True
         
         #print(me.val)
         #print(me.left.val) if me.left is not None else print("left: None")
         #print(me.right.val) if me.right is not None else print("right: None")
         #print(parents_lt)
         #print(parents_gt)
         #print('---')
         for p in parents_lt:
             if p.val >= me.val:
                 print('a')
                 return False
         
         for p in parents_gt:
             if p.val <= me.val:
                 print('b')
                 return False
         
         if me.left is not None:
             if me.left.val >= me.val:
                 print('c')
                 return False
             
         if me.right is not None:
             if me.right.val <= me.val:
                 print('d')
                 return False
         gt2 = parents_gt + [me]
         lt2 = parents_lt + [me]
         return self.valid(me.left, parents_lt, gt2) and self.valid(me.right, lt2, parents_gt)
         
     
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         if root is None:
             return True        
         
         return self.valid(root, list(), list())
