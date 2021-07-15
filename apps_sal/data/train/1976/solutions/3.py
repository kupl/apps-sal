class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.tier=[None]*27
         
 
     def buildDict(self, dict):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         for word in dict:
             p=self.tier
             for c in word:
                 t=ord(c)-ord('a')
                 if not p[t]:
                     p[t]=[None]*27
                 p=p[t]
             p[26]=1
         
 
     def search(self, word):
         """
         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
         :type word: str
         :rtype: bool
         """
         def func(w):
             p=self.tier
             for c in w:
                 t=ord(c)-ord('a')
                 if not p[t]:
                     return False
                 p=p[t]
             return p[26]==1
         pool='abcdefghijklmnopqrstuvwxyz'
         for i in range(len(word)):
             for cc in pool:
                 if cc!=word[i]:
                     tt=word[:i]+'%c'%cc+word[i+1:]
                     if func(tt):
                         return True
         return False
             
         
 
 
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)

