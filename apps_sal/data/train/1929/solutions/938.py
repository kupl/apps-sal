class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self.create_trie(words)
        self.l = []

    def create_trie(self, words):
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr['.'] = True
        return trie
            
        
    def query(self, letter: str) -> bool:
        self.l.append(self.trie)
        new_list = []
        is_word = False
        for trie in self.l:
            if letter in trie:
                new_list.append(trie[letter])
                is_word |= '.' in trie[letter]
        self.l = new_list
        return is_word
                
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

