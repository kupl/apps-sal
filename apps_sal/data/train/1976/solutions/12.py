class Trie():
     def __init__(self):
         self.mark = list()
         self.children = {}
 
 class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.root = Trie()
         
 
     def buildDict(self, dict):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         node = self.root
         for word in dict:
             words = {}
             for i in range(len(word)):
                 words[word[:i] + "_" + word[i+1:]] = word[i]
             for word in words:
                 node = self.root
                 for c in word:
                     node = node.children.setdefault(c,Trie()) 
                 node.mark.append(words[word])
         
         
 
     def search(self, word):
         """
         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
         :type word: str
         :rtype: bool
         """
         words = dict()
         for i in range(len(word)):
             words[word[:i] + "_" + word[i+1:]] = word[i]
         for word in words:
             node = self.root
             for c in word:
                 node = node.children.get(c) 
                 if not node:
                     break
             else:
                 if node.mark != list() and [words[word]] != node.mark:
                     return True
         return False
         
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)
