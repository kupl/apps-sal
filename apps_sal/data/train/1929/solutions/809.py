class StreamChecker:

    def __init__(self, words: List[str]):
        self.watchlist = []
        self.trie = {}
        for word in words:
            temp = self.trie
            for c in word:
                temp.setdefault(c, {})
                temp = temp[c]
            temp.setdefault(\"#\",)
        

    def query(self, letter: str) -> bool:
        watchlist = []
        
        if letter in self.trie:
            watchlist.append(self.trie[letter])

        for node in self.watchlist:
            if letter in node:
                watchlist.append(node[letter])

        self.watchlist = watchlist
        
        return any(\"#\" in n for n in self.watchlist)
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
