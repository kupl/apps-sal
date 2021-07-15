# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         if n == 0:
             return []
         rtnList = []
         for i in range(n,0,-1):
             newList = []
             if rtnList == []:
                 newList = [TreeNode(i)]
             else:
                 for t in rtnList:
                     newList += self.insertNode(t, i)
             rtnList = newList
         return rtnList
     
     def insertNode(self, tree, i):
         """
         insert node to the bottom left
         """
         p = tree
         rtnTree = []
         node = TreeNode(i)
         node.right = self.copyTree(tree)
         rtnTree += node,
         while True:
             node = TreeNode(i)
             newTree = self.copyTree(tree)
             newP = newTree
             while newP.val != p.val:
                 newP = newP.left
             node.right = newP.left
             newP.left = node
             rtnTree += newTree,
             if p.left:
                 p = p.left
             else:
                 break
         return rtnTree
         
         
     
     def copyTree(self,tree):
         newTree = None
         if tree:
             newTree = TreeNode(tree.val)
         if tree.left:
             newTree.left = self.copyTree(tree.left)
         if tree.right:
             newTree.right = self.copyTree(tree.right)
         return newTree
             
         
