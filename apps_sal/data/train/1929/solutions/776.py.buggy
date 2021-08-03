class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr[\"$\"] = True
        self.prev_tries = []
        

    def query(self, letter: str) -> bool:
        curr_trie = []
        self.prev_tries.append(self.trie)
        is_present = False
        
        for trie in self.prev_tries:
            if letter in trie:
                if  '$' in trie[letter]:
                    is_present = True
                curr_trie.append(trie[letter])
        
        self.prev_tries = curr_trie[:]
        
        return is_present

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
