from collections import defaultdict
 # Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     """
     :type root: TreeNode
     :rtype: map{sum:int : frequency:int} 
     """
     def __init__(self):
         self._iter = 0
     def getAllSums(self, root):
         if not root:
             return defaultdict(int), 0
         all_sums, left_sum = self.getAllSums(root.left)
         all_right_sums, right_sum = self.getAllSums(root.right)    
         # mege both maps
         for key,val in all_right_sums.items():
             all_sums[key] += val
         cur_sum = right_sum + root.val + left_sum
         all_sums[cur_sum] += 1
         return all_sums, cur_sum
         
     def findFrequentTreeSum(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         all_sums,_ = self.getAllSums(root)
         result = []
         max_occurence = 0
         for key,val in all_sums.items():
             max_occurence = max(max_occurence,val)
         for key,val in all_sums.items():
             if val == max_occurence:
                 result.append(key)
         return result
         
