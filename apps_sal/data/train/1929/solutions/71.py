class StreamChecker:
    
            

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            startTrie = self.trie
            for c in word:
                if c not in startTrie:
                    startTrie[c] = {}
                startTrie = startTrie[c]
            startTrie[\"isEnd\"] = True
        self.openTries = []
        # print(self.trie)

    def query(self, letter: str) -> bool:
        
        # print(self.openTries)
        
        #Insert this new letter into our tries.
        if letter in self.trie:
            self.openTries.append(self.trie)
        
        #Increment these tries that are still open.
        found = False
        tempTries = []
        while self.openTries:
            trie = self.openTries.pop()
            if letter in trie:
                trie = trie[letter]
                if \"isEnd\" in trie:
                    found = True
                tempTries.append(trie)
        self.openTries = tempTries
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
