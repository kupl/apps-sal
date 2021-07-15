import math
 class Solution:
     def numRabbits(self, answers):
         """
         :type answers: List[int]
         :rtype: int
         """
         
         colorGroup = collections.defaultdict(int)
         for answer in answers:
             colorGroup[answer] += 1
         toReturn = 0
         for key in colorGroup:
             claimedBuddies, claimer = key, colorGroup[key]
             ## print(claimedBuddies)
             ## print(claimer)
             toReturn += math.ceil(claimer/(claimedBuddies+1))*(claimedBuddies+1)
             ## print(toReturn)
             ## print()
         return toReturn
