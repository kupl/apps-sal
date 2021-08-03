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
         
         if n < 1: return []
         
         def genTrees(trees, i, j):
             if (i, j) in trees: return trees[(i, j)]
             if i > j: return [None]
             
             trees[(i, j)] = []
             
             for k in range(i, j + 1):
                 leftTrees = genTrees(trees, i, k-1) 
                 rightTrees = genTrees(trees, k+1, j)
                 newTrees = []
                 for l in leftTrees:
                     for r in rightTrees:
                         newNode = TreeNode(k)
                         newNode.left = l
                         newNode.right = r
                         newTrees.append(newNode)
                 trees[(i, j)] += newTrees
                 
             return trees[(i, j)]
         
         trees = {}
         return genTrees(trees, 1, n)
         
         
