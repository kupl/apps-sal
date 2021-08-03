# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         res=[];
         self.kthRec(root,res);
         return res[k-1];
     
     def kthRec(self,root,res):
         if(root!=None):
             self.kthRec(root.left,res);
             res.append(root.val);
             self.kthRec(root.right,res);
             
