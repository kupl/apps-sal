class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])
        
        # O(NM) time and space N=len(words), M = wordlen #
        for w in words:
            node = self.trie
            for c in w[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = w

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        # O(M) time and space 
        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

