class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie_head = {}
        self.trie_leaf = '$'
        
        for word in words:
            trie_node = self.trie_head
            
            for c in word:
                trie_node = trie_node.setdefault(c, {})
            
            trie_node[self.trie_leaf] = self.trie_leaf
        
        self.trie_pointers = []
        

    def query(self, letter: str) -> bool:
        # Advance all existing pointers
        self.trie_pointers = [trie_node[letter] for trie_node in self.trie_pointers if letter in trie_node]
        
        if letter in self.trie_head:
            self.trie_pointers.append(self.trie_head[letter])
            
        return any([(self.trie_leaf in trie_node) for trie_node in self.trie_pointers])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

