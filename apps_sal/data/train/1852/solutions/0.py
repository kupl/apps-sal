"""
 of course this is a dp problem.
 if we consider upper bound and lower bound for each sub tree, 
 we will have a index-based solution over all posible numbers.
 
 each time we part a sub-tree into two parts, the question then becomes:
 how many possible boundaries can we find (start, end).
 """
 
 class Solution:
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         dp = dict()
         ret = self.generate_recursively(list(range(1, n+1)), 0, n, dp)
         if n == 0:
             ret = []
         return ret
 
     # list is a sorted list of trees
     def generate_recursively(self, l, start, end, dp):
         ret = []
         if end - start == 1:
             ret = [TreeNode(l[start]),]
         elif end - start <= 0:
             ret = [None,]
 
         # take each index as partition place
         else:
             for idx in range(0, end - start):
                 left_nodes = dp[(start, start+idx)] if (start, start+idx) in dp.keys() else self.generate_recursively(l, start, start+idx, dp)
                 right_nodes = dp[(start+idx+1, end)] if (start+idx+1, end) in dp.keys() else self.generate_recursively(l, start+idx+1, end, dp)
 
                 for left in left_nodes:
                     for right in right_nodes:
                         root = TreeNode(l[start+idx])
                         root.left = left 
                         # if left != '<E>' else None
                         root.right = right 
                         # if right !='<E>' else None
                         ret.append(root)
         dp[(start, end)] = ret
         return ret
 
 s = Solution()
 s.generateTrees(3)
