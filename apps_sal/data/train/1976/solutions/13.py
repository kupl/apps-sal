class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.dict = collections.defaultdict(list)
 
     def buildDict(self, dict):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         for word in dict:
             self.dict[len(word)].append(word)
 
     def search(self, word):
         """
         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
         :type word: str
         :rtype: bool
         """
         n = len(word)
         print((word, self.dict[n]))
         for item in self.dict[n]:
             count = 0
             for i in range(n):
                 if count > 1: continue
                 if item[i] != word[i]: count += 1
             if count == 1:
                 return True
         return False
                     
         
 
 
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)

