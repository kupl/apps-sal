class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.pointers = list()
        for word in words:
            node = self.trie
            for c in word:
                node = node.setdefault(c, {})
            
            node[\"#\"] = True
    
    def query(self, letter: str) -> bool:
        res = False
        self.pointers = [node[letter] for node in self.pointers if letter in node]
        res = res or any(\"#\" in node for node in self.pointers)
        
        if letter in self.trie:
            node = self.trie[letter]
            res = res or (\"#\" in node)
            self.pointers.append(node)
        
        return res

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
