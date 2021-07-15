class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitlist = []
        self.trie = {}
        for word in words:
            t = self.trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = \"#\"
        
    def query(self, letter: str) -> bool:
        waitlist = []
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
        self.waitlist = waitlist
        return any(\"#\" in i for i in self.waitlist)
        
