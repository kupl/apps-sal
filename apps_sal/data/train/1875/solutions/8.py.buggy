# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
   def findFrequentTreeSum(self, root):
     from collections import defaultdict
     f = defaultdict(int)    
     def treeSum(root):
       if not root: return 0
       s = root.val + treeSum(root.left) + treeSum(root.right)
       f[s] += 1   
       return s
     treeSum(root)
     ans = []
     if not f: return ans    
     max_freq = max(f.values())    
     for s in f:
       if f[s] == max_freq: 
         ans.append(s)
     return ans
     
         
