class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = {}
        # self.max_len = 0
        self.buff = \"\"
        for word in words:
            # self.max_len = max(self.max_len , len(word))
            cur = self.root
            
            for w in word[::-1]:
                cur = cur.setdefault(w, {})
            cur['*'] = '*'
            
        # print(self.root)
            
    
        
        

    def query(self, letter: str) -> bool:
        self.buff = letter + self.buff 
        # if len(self.buff) > self.max_len:
        #     self.buff.pop(0)

        def dfs(i, cur):
            if i == len(self.buff):
                return '*' in cur
            
            if '*' in cur:
                return True
            
            if self.buff[i] not in cur:
                return False
            
            return dfs(i + 1, cur[self.buff[i]])
        
        # self.buff = ['a','b']
        # print(self.buff)
        return dfs(0, self.root)
        
        
        # for i in range(len(self.buff)):
        #     if self.buff[i] in self.root:
        #         # print(i)
        #         # print(i,self.buff[i:])
        #         if dfs(i, self.root) == True:
        #             return True
        # return False
    
# class TrieNode:
#     def __init__(self):
#         self.dic = {}
#         self.end = False
        
# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.root = TrieNode()
#         for word in words:
#             word = \"\".join(reversed(word))
#             self.addword(word)
#         self.stream = \"\"
            
#     def addword(self, word):
#         current = self.root
#         for char in word:
#             if char not in current.dic:
#                 current.dic[char] = TrieNode()
#             current = current.dic[char]
#         current.end = True
            
#     def helper(self, current, stream):
#         for i in range(len(stream)):
#             if stream[i] not in current.dic: 
#                 if current.end:
#                     return True
#                 else:
#                     return False
#             else:
#                 if current.end:
#                     return True
#             current = current.dic[stream[i]]
#         return current.end
        
#     def query(self, letter: str) -> bool:
#         self.stream = letter + self.stream
#         return self.helper(self.root, self.stream)      

        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
