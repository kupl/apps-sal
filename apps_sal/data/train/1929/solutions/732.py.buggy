# class TrieNode:
#     def __init__(self):
#         self.children = [None]*26
#         self.end = False

# class StreamChecker:

#     def char_to_index(self,ch):
#         return ord(ch) - ord('a')
    
#     def insert(self,word):
#         n = len(word)    
#         ptr = self.root
#         for lvl in range(len(word)):
#             i = self.char_to_index(word[lvl])
#             if ptr and not ptr.children[i]:
#                 ptr.children[i] = TrieNode()
                
#             ptr = ptr.children[i]
            
#         ptr.end = True
        
#     def __init__(self, words: List[str]):
#         self.root = TrieNode
        
#         for word in words:
#             self.insert(word)
#         self.pe = None

#     def query(self, letter: str) -> bool:
        
#         if self.pe and self.pe.children[char_to_index(letter)]:
#             if self.pe.end:
#                 return True
#             self.pe = self.pe.children[char_to_index(letter)]
#             return False
        
#         if self.root.children[char_to_index(letter)]:
#             self.pe = self.root.children[char_to_index(letter)]
#             if self.root.end:
#                 return True
#             return False
            
        


# # Your StreamChecker object will be instantiated and called as such:
# # obj = StreamChecker(words)
# # param_1 = obj.query(letter)


class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)
