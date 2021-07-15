# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findFrequentTreeSum(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         if not root: return []
         D = dict()
         def AccuTree(root):
             if not root: return 0
             leftA = AccuTree(root.left)
             rightA = AccuTree(root.right)
             Accu = leftA + rightA + root.val
             if D.get(Accu): D[Accu] += 1
             else: D[Accu] = 1
             return Accu
         AccuTree(root)
         maxVal = max(D.values())
         return [x for x in D.keys() if D[x] == maxVal]
