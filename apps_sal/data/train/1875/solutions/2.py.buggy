# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 from collections import defaultdict
 
 class Solution:
   def findFrequentTreeSum(self, root):
     """
     :type root: TreeNode
     :rtype: List[int]
     """
     def get_sum(node):
       if node == None:
         return 0
       sum = node.val + get_sum(node.left) + get_sum(node.right)
       sum_freq[sum] += 1
       return sum
 
     # Calculate sum for all subtrees and save them in dict `sum_freq`
     sum_freq = defaultdict(lambda: 0)
     get_sum(root)
     if not sum_freq:
       return []
     # Filter sums by the highest frequency
     max_freq = max(sum_freq.values())
     return [sum for (sum, freq) in sum_freq.items() if freq == max_freq]
 

