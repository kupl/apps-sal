class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = ''
        self.trie = {}
        
        # Initialize trie with words
        curr = self.trie
        for word in words:
            # Add reverse of word
            for char in word[::-1]:
                curr.setdefault(char, {})
                curr = curr[char]
            curr['end'] = True
            curr = self.trie
            
        # print(self.trie)
        
    def query(self, letter: str) -> bool:
        self.stream += letter
        
        def _search(string, curr):
            if 'end' in curr:
                return True
            
            if string and string[0] in curr:
                return _search(string[1:], curr[string[0]])
            
            return False
        
        
        return _search(self.stream[::-1], self.trie)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

