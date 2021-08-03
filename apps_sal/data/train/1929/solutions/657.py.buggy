class StreamChecker:
    
    openDicts = []
    cache = {}
    words = []
    acc = \"\"
    
    def __init__(self, words: List[str]):
        self.t = {}
        self.acc = \"\"
        for w in words:
            d = self.t
            for c in w[::-1]:
                d[c] = d.get(c, {})
                d = d[c]
            d['end'] = True    
        self.openDicts = [self.t]
        self.words = words
        # print(self.t)
        
    def query(self, letter: str) -> bool:
        self.acc += letter
        d = self.t
        for c in self.acc[::-1]:
            if 'end' in d:
                return True
            elif c in d:
                d = d[c]
            else:
                return False
        return 'end' in d    
            
        
        
        
#         def check(a) -> bool:
#             d = self.t
#             for i, c in enumerate(a[::-1]):
#                 if c in d:
#                     d = d[c]
#                 else:
#                     return False
#             self.cache[a] = d
#             return 'end' in d    
        
#         for i in range(len(self.acc)):
#             if check(tuple(self.acc[i:])):
#                 return True
        
#         return False
        
        
#         print('=== ', letter)
#         toDel = []
#         toAppend = []
#         foundEnd = False
#         for i, d in enumerate(self.openDicts):
#             if letter in d:
#                 print('found', letter)
#                 toAppend.append(d[letter])
#                 print(toAppend)
#                 if 'end' in d[letter]:
#                     foundEnd = True
#             else:
#                 toDel.append(i)
        
#         toDel.sort(reverse=True)
#         for i in toDel:
#             if self.openDicts[i] != self.t:
#                 del self.openDicts[i]
#                 print('del', i)
#         for a in toAppend:
#             self.openDicts.append(a)
        
#         print('after del', self.openDicts)
#         print('>>=== ', letter)
#         return foundEnd
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
