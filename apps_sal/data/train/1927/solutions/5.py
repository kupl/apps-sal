class Solution:
     def asteroidCollision(self, asteroids):
         """
         :type asteroids: List[int]
         :rtype: List[int]
         """
         if not asteroids:
             return asteroids
 
         remaining = []
         for item in asteroids:
                             
             itemSign, itemVal = self.getItemDetails(item)
             shouldAppend = False
 
             while True:
                 if not remaining:
                     shouldAppend = True
                     break
                 
                 topSign, topVal = self.getItemDetails(remaining[-1])
 
                 if not (topSign and not itemSign):
                     shouldAppend = True
                     break
 
                 if topVal > itemVal:
                     break
                 elif topVal == itemVal:
                     remaining.pop()
                     break
                 else:
                     remaining.pop()
                                                                     
             if shouldAppend:
                 remaining.append(item)
 
         return remaining
 
     def getItemDetails(self, val):
         return val > 0, abs(val)
