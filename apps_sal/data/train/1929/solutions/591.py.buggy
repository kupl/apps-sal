class StreamChecker:


#     def __init__(self, words: List[str]):
#         self.root = {}
#         self.end = -1
#         for w in words:
#             self.insert(w)
#         self.qhist = ''

#     def insert(self, word):
#         curNode = self.root
#         for c in word[::-1]:
#             if not c in curNode:
#                 curNode[c] = {}
#             curNode = curNode[c]
#         curNode[self.end] = True

#     def query(self, letter: str) -> bool:
#         self.qhist += letter
#         curNode = self.root
#         for c in self.qhist[::-1]:
#             if not c in curNode:
#                 return False
#             curNode = curNode[c]
#             if self.end in curNode:
#                 return True
    def __init__(self, words: List[str]):
        self.dic = {}
        for word in words:
            if word[-1] not in self.dic:
                self.dic[word[-1]] = [word[:-1]]
            else:
                self.dic[word[-1]].append(word[:-1])
        
        self.string = \"\"

    def query(self, letter: str) -> bool:
        self.string += letter
        if letter in self.dic:
            for word in self.dic[letter]:
                length = len(word) + 1
                complete_word = word + letter
                if len(self.string) >= length and complete_word == self.string[- length:]:
                    return True
            return False
        else:
            return False



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
