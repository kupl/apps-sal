class Solution:
     def wordPattern(self, pattern, str):
         if not pattern and not str:
             return True
         if not pattern or not str:
             return False
         
         str_list = str.split()
         if len(pattern) != len(str_list):
             return False
         
         pattern_table = collections.defaultdict(int)
         str_table = collections.defaultdict(int)
         for idx in range(len(pattern)):
             if pattern_table[pattern[idx]] != str_table[str_list[idx]]:
                 return False
             pattern_table[pattern[idx]] = idx + 1
             str_table[str_list[idx]] = idx + 1
             
         return True
         
         """
         :type pattern: str
         :type str: str
         :rtype: bool
         """

