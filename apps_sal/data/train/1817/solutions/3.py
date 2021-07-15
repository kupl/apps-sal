import queue
 
 class CountPair:
     def __init__(self, key, count):
         self.key = key
         self.count = count
     def __lt__(self, other):
         return self.count > other.count
 
 class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         c_hash = {}
         q = queue.PriorityQueue()
         for c in S:
             if c not in c_hash:
                 c_hash[c] = 1
             else:
                 c_hash[c] += 1
         for k in c_hash:
             tmp = CountPair(k,c_hash[k])
             q.put(tmp)
         result = "#"
         for i in range(len(S)):
             v = q.get()
             if v.count==0:
                 return ""
             if result[-1] != v.key:
                 result += v.key
                 v.count -= 1
                 if v.count != 0:
                     q.put(v)
             else:
                 if q.empty():
                     return ""
                 v2 = q.get()
                 result += v2.key
                 v2.count -= 1
                 if v2.count != 0:
                     q.put(v2)
                 q.put(v)
         return result[1:]
             
                 
         
         
         
         
         
         
         
         
