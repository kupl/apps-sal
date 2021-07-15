class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.waitlist = []
        for word in words:
            head = self.trie
            for char in word:
                if char not in head:
                    head[char] = {}
                head = head[char]
            head['#'] = '#'

    def query(self, letter: str) -> bool:
        waitlist = []
        # if letter can be the prefix of word
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        # for each possible prefix, append letter if the new substr still can be a prefix
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
                
        self.waitlist = waitlist
        return any('#' in item for item in self.waitlist)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter) 

