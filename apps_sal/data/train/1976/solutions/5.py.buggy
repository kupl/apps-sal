from collections import defaultdict
 
 class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.magic_dict = defaultdict(list)
 
     def buildDict(self, words):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         for word in words:
             for i in range(len(word)):
                 self.magic_dict[word[:i] + '*' + word[i+1:]].append(word[i])
 
     def search(self, word):
         for i, char in enumerate(word):
             candidates = self.magic_dict[word[:i] + '*' + word[i+1:]]
             for origin in candidates:
                 if origin != char:
                     return True
         return False
         
         
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)
