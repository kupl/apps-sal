# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def splitBST(self, root,target):
         """
         :type root: TreeNode
         :type V: int
         :rtype: List[TreeNode]
         """
         
         def split_bst_recur(root, target):
             if not root:
                 return (None, None)
             
             if not root.left and not root.right:
                 if root.val <= target:
                     return (root, None)
                 else:
                     return(None, root)
             
             if root.val > target:
                 l, r = split_bst_recur(root.left, target)
                 root.left = r
                 return (l, root)
             else:
                 l, r = split_bst_recur(root.right, target)
                 root.right = l
                 return (root, r)
         
         if not root:
             return [[],[]]
         
         l, r = split_bst_recur(root, target)
         return [l, r]
             

