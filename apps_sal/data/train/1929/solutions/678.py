class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            p = self.trie
            for c in word:
                if c not in p: p[c] = {}
                p = p[c]
            
            p['$'] = True
        
        self.pointers = []
        
    def query(self, letter: str) -> bool:
        self.pointers.append(self.trie)
        
        new_pointers = []
        found = False
        for pointer in self.pointers:
            if letter in pointer:
                new_pointers.append(pointer[letter])
                if '$' in pointer[letter]: found = True
        self.pointers = new_pointers
        return found
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

