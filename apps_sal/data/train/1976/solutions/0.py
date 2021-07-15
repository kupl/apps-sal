class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.l = []
 
     def buildDict(self, dict):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         self.l= dict
 
     def search(self, word):
         """
         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
         :type word: str
         :rtype: bool
         """
         def diffnumber(a,b):
             count = 0
             for i in range(len(a)):
                 if a[i] !=b[i]:
                     count +=1
             return count
         for x in self.l:
             if len(x) == len(word) and diffnumber(x,word) ==1:
                 return True
         return False
                 
                 
         
 
 
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)

