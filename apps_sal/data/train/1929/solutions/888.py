class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node['.'] = '.'

        self.syms = []

    def query(self, letter: str) -> bool:
        trie, syms = self.trie, self.syms
        
        syms.append(letter)
        
        node = trie
        for c in syms[::-1]:
            if c not in node:
                return False
            node = node[c]
            if '.' in node:
                return True
        
        return False

# Runtime: 5832 ms, faster than 13.42% of Python3 online submissions for Stream of Characters.
# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.trie = dict()
#         for word in words:
#             node = self.trie
#             for c in word:
#                 if c not in node:
#                     node[c] = dict()
#                 node = node[c]
#             node['.'] = '.'

#         self.curs = []

#     def query(self, letter: str) -> bool:
#         trie, curs = self.trie, self.curs
        
#         curs = [cur[letter] for cur in curs if letter in cur]
#         if letter in trie:
#             curs.append(trie[letter])
#         self.curs = curs

#         return any('.' in cur for cur in curs)

