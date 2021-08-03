class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = \"\"
        self.max_len = max(len(word) for word in words)
        self.trie = {}
        self._build_trie(words)
        
    def query(self, letter: str) -> bool:
        self.stream += letter
        if len(self.stream) > self.max_len:
            self.stream = self.stream[1:]
            
        node = self.trie
        for char in self.stream[::-1]:
            if '$' in node:
                return True
            elif char not in node:
                return False
            else:
                node = node[char]
        
        return '$' in node
        
    def _build_trie(self, words: List[str]):
        for word in words:
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word
    

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
