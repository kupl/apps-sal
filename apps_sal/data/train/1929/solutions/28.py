class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.wl = []
        for word in words:
            trie = self.trie
            for w in word:
                trie[w] = trie.get(w, dict())
                trie = trie[w]
            trie[\"#\"] = '#'
        
        # print(self.trie)
        

    def query(self, letter: str) -> bool:
        # print(letter, self.wl)
        wl = []
        if letter in self.trie:
            wl.append(self.trie[letter])
        
        for i in self.wl:
            
            if letter in i:
                wl.append(i[letter])
        
        self.wl = wl
        
        return any('#' in i for i in self.wl)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
