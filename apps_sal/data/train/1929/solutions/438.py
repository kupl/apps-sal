class StreamChecker:

    def __init__(self, words: List[str]):
        self.query_letters = []
        # post-fix hash table
        self.hash = {}
        for w in words:
            for i in range(len(w)-1, -1, -1):
                if i == 0: self.hash[w[i:]] = True
                elif w[i:] in self.hash: continue
                else: self.hash[w[i:]] = False
        # print(self.hash)

    def query(self, letter: str) -> bool:
        self.query_letters.append(letter)
        length = len(self.query_letters)
        for i in range(length-1, -1, -1):
            ls = \"\".join(self.query_letters[i:])
            if ls not in self.hash: 
                return False
            if self.hash[ls]: return True
        return False


#     def __init__(self, words: List[str]):
#         self.Trie={}
#         for word in words:
#             curnode=self.Trie
#             word=word[::-1]
#             print(word)
#             for ch in word:
#                 if ch not in curnode:
#                     curnode[ch]={}
#                 curnode=curnode[ch]
#             curnode['#']=1 # '#' means the end of a word
#         self.pre=''
 
#     def query(self, letter: str) -> bool:
#         self.pre=self.pre+letter
#         curnode=self.Trie
#         print(curnode)
#         # print(self.pre)
#         for i in range(0,len(self.pre)):
#             if self.pre[-i-1] not in curnode:
#                 break
#             curnode=curnode[self.pre[-i-1]]
#             print(curnode)
#             if '#' in curnode:
#                 return True
#         return False

        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
