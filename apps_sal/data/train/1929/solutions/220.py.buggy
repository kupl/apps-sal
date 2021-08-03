class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self._get_trie(words)
        self.stream = collections.deque()
    
    def _get_trie(self, words):
        trie = ({}, False)
        
        for w in words:
            cur = trie
            n = len(w)
            for i, c in enumerate(w[::-1]): 
                \"\"\"
                reversing the word is crucial for runtime
                \"\"\" 
                is_last_letter = i == n - 1
                
                if c not in cur[0]:
                    cur[0][c] = ({}, is_last_letter)
                elif c in cur[0] and not cur[0][c][1] and is_last_letter:
                    cur[0][c] = (cur[0][c][0], is_last_letter)
                
                cur = cur[0][c]
            
        return trie
    
#     def _search(self, word):
#         cur = self.trie
#         for c in word:
#             if c in cur[0]:
#                 cur = cur[0][c]
#             else:
#                 return (False, False)
        
#         return (cur[1], True)

    
    def _search_any(self, word):
        cur = self.trie
        for c in word:
            if c in cur[0]:
                cur = cur[0][c]
            else:
                return False
            
            if cur[1]:
                return True
        
        return False

#     def query_2(self, letter: str) -> bool:
#         self.stream.append(letter)
#         word = copy.copy(self.stream)
#         word_seen = False
#         for i in range(len(self.stream)):
#             search = self._search(word)
#             if search[0]:
#                 return True
#             if not search[1] and not word_seen:
#                 self.stream.popleft()
#             else:
#                 word_seen = True
#             word.popleft()
        
#         return False
    
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self._search_any(self.stream)



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
