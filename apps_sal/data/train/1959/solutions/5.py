# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         theValues = []
         def inorder(node):
             if(node!=None):
                 inorder(node.left)
                 theValues.append(node.val)
                 inorder(node.right)
         inorder(root)
         minDiff = sys.maxsize
         for i in range(len(theValues)-1):
             minDiff = min(minDiff, theValues[i+1]-theValues[i])
         return minDiff
