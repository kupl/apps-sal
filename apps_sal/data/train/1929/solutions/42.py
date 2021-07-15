class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)
# class Trie:
#     def __init__(self):
#         self.trie = {}
        
#     def add_word(self,word):
#         nextLevel = self.trie
#         for i,char in enumerate(word):
#             isWord = i == len(word) - 1
#             if char in nextLevel:
#                 if isWord:
#                     nextLevel[char].isWord = True
#                 nextLevel = nextLevel[char].children
#             else:
#                 node = TrieNode(char, isWord)
#                 nextLevel[char] = node
#                 nextLevel = nextLevel[char].children
            
        
# class TrieNode:
#     def __init__(self, char, isWord = False):
#         self.char = char
#         self.isWord = isWord
#         self.children = {}


# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.words = set(words)
#         self.trie = Trie()
#         for word in words:
#             self.trie.add_word(word)
            
#         self.nextLevels = []

#     def query(self, letter: str) -> bool:
#         print(len(self.nextLevels))
#         nextLevels = []
#         isWord = False
#         if len(self.nextLevels):
#             for level in self.nextLevels:
#                 if letter in level:
#                     if level[letter].isWord:
#                         isWord = True
#                     nextLevels.append(level[letter].children)
        
#         if letter in self.trie.trie:
#             nextLevels.append( self.trie.trie[letter].children )
#             if self.trie.trie[letter].isWord:
#                 isWord = True
                
#         self.nextLevels = nextLevels
    
#         return isWord
    

