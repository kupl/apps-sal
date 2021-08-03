class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self.buildTrie(words)
        self.waitlist = [] # queue
        
        
    def buildTrie(self, words):
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                curr = curr.setdefault(ch, {})
            curr[\"#\"] = \"#\"
        return trie
        
        
    def query(self, letter: str) -> bool:
        waitlist = []
        
        # check if letter is at the root 
        if letter in self.trie:
            waitlist.append(self.trie[letter])
            
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
            
        self.waitlist = waitlist
        return any(\"#\" in item for item in self.waitlist)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
