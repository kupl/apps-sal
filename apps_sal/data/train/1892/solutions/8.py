# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         self.ret=[]
         self.DFS(root,sum,[])
         return(self.ret)
     def DFS(self,roots,nums,valList):
         if(roots==None):
             return()
         if(roots.left==None and roots.right==None and nums==roots.val):
             self.ret.append(valList+[roots.val])
         self.DFS(roots.left,nums-roots.val,valList+[roots.val])
         self.DFS(roots.right,nums-roots.val,valList+[roots.val])
         
         
         
