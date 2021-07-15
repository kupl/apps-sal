class Solution:
     def numRabbits(self, answers):
         """
         :type answers: List[int]
         :rtype: int
         """
         counter = [0 for i in range(1000)]
         for i in answers:
             counter[i] += 1
         num = 0
         for k, v in enumerate(counter):
             d, m = divmod(v, k + 1)
             if d > 0:
                 num += (k + 1) * d
             if m > 0:
                 num += k + 1
         return num
             

