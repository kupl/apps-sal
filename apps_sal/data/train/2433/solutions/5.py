class Solution:
     def licenseKeyFormatting(self, S, K):
         """
         :type S: str
         :type K: int
         :rtype: str
         """
         char_list = self.getChars(S)
         num_groups = len(char_list) // K
         group_1_cnt = len(char_list) % K
         
         output = ""
         if group_1_cnt > 0:
             output += char_list[0:group_1_cnt]
             if num_groups > 0:
                 output += "-"
             
         for i in range(1, num_groups + 1):
             start = i * K + group_1_cnt - K
             finish = start + K
             output += char_list[start:finish]
             if i != num_groups:
                 output += "-"
                 
         return output
         
     def getChars(self, S):
         char_list = ""
         
         for char in S:
             if char != "-":
                 char_list += char.upper()
         
         return char_list

