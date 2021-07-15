class Solution:
     def findLongestChain(self, pairs):
         """
         :type pairs: List[List[int]]
         :rtype: int
         """
         queue = collections.deque(sorted(pairs, key=lambda pair: pair[1]))
         
         count = 0
         
         while len(queue) > 0:
           count += 1
           curr = queue.popleft()
           while len(queue) > 0 and queue[0][0] <= curr[1]:
             queue.popleft()
         
         return count
           
         

