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
         if root == None: return []
         m = collections.defaultdict(int)
         self.helper(root, m)
         max_value = max(m.values())
         res = []
         for v in m.keys():
             if m[v] == max_value:
                 res.append(v)
         return res
         
     def helper(self, node, m):
         if not node:
             return 0
         left, right = self.helper(node.left, m), self.helper(node.right, m)
         m[node.val+left+right]+=1
         return node.val + left + right
