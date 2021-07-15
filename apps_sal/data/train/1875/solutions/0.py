class Solution:
 
     def findFrequentTreeSum(self, root):
         self.sums = []
         if not root:
             return []
         self.traverse(root)
         res = collections.Counter(self.sums)
         frequent = max(res.values())
         return [x for x in res if res[x] == frequent]
 
 
     def traverse(self, root):
         if not root:
             return 0
         
         self_sum = root.val + self.traverse(root.left) + self.traverse(root.right)
 
         self.sums.append(self_sum)
         return self_sum

