class Solution:
     def wordPattern(self, pattern, str):
         """
         :type pattern: str
         :type str: str
         :rtype: bool
         """
         pattern_map = {}
         pattern_word = []
         pattern_result = []
         string_map = {}
         string_word = []
         string_result = []
         for index,item in enumerate(pattern):
             if item not in pattern_map:
                 pattern_word.append(item)
             pattern_map[item] = pattern_map.get(item,[]) + [index]
         for item in pattern_word:
             pattern_result.append([pattern_map[item]])
         start = 0
         count = 0
         index = 0
         while index <= len(str):
             if index < len(str) and str[index] != ' ':
                 index += 1
                 continue
             else:
                 sub_str = str[start:index]
                 index += 1
                 if sub_str not in string_map:
                     string_word.append(sub_str)
                 string_map[sub_str] = string_map.get(sub_str,[]) + [count]
                 start = index
                 count += 1
         for item in string_word:
             string_result.append([string_map[item]])
         if string_result == pattern_result:
             return True
         else:
             return False
                 
             

