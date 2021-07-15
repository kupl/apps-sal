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
         if not n:
             return []
         all_tress = {}
         for r in range(1, n+1):
             for start in range(1, n+2-r):
                 end = start + r - 1
                 all_tress[self.to_key(start, end)] = []
                 if r == 1:
                     all_tress[str(start) + str(end)] = [TreeNode(start)]
                 else:
                     for index_root in range(start, end + 1):
                         left_trees = all_tress.get(self.to_key(start, index_root - 1), [None])
                         right_trees = all_tress.get(self.to_key(index_root + 1, end), [None])
                         for left_tree in left_trees:
                             for right_tree in right_trees:
                                 new_root = TreeNode(index_root)
                                 new_root.left = left_tree
                                 new_root.right = right_tree
                                 all_tress[self.to_key(start, end)].append(new_root)
         return all_tress.get(self.to_key(1, n))
 
     def to_key(self, start, end):
         return str(start) + str(end)
