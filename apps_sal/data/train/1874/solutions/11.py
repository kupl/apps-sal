class Solution:
     def numRabbits(self, answers):
         """
         :type answers: List[int]
         :rtype: int
         """
         dic = dict()
         for answer in answers:
             if answer in dic:
                 dic[answer] += 1
             else:
                 dic[answer] = 1
         ans = 0
         for answer in dic:
             ans += math.ceil(dic[answer] / (answer + 1)) * (answer + 1)
         return ans
