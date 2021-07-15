# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 import sys
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.res = sys.maxsize;
         self.prevVal = -sys.maxsize;
         
         def in_order(root):
             if not root: return;
             in_order(root.left);
             
             diff = root.val - self.prevVal;
             self.prevVal = root.val
             self.res = min(self.res, diff);
             
             in_order(root.right);
             
         in_order(root);
         return self.res;
