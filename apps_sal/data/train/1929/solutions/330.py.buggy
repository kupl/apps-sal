# 1032. Stream of Characters

# class TrieNode:
#     def __init__(self, val=None, isEnd=False):
#         self.val = val
#         self.isEnd = isEnd
#         self.next = {}

# Solution 4: Construct Trie with Reversed Words
# Time: 600 ~ 700ms
# Time complexity: O(WQ)

# Python
class StreamChecker:
    
    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.S = \"\"
        self.W = max(map(len, words))

    def query(self, letter):
        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#'] == True:
                    return True
            else:
                break
        return False

# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.trie = {}
#         self.stream = deque([])

#         for word in set(words):
#             node = self.trie       
#             for ch in word[::-1]:
#                 if not ch in node:
#                     node[ch] = {}
#                 node = node[ch]
#             node['$'] = word
        
        
#     def query(self, letter: str) -> bool:
#         self.stream.appendleft(letter)
        
#         node = self.trie
#         for ch in self.stream:
#             if '$' in node:
#                 return True
#             if not ch in node:
#                 return False
#             node = node[ch]
#         return '$' in node
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
