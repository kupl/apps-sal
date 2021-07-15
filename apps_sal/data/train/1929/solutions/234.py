class StreamChecker:

    def build_trie(self, words):
        for word in words:
            w = word[::-1]
            curr = self.trie
            for l in w:
                if curr[ord(l)-ord('a')]:
                    curr = curr[ord(l)-ord('a')]
                else:
                    curr[ord(l)-ord('a')] = [[] for i in range(27)]
                    curr = curr[ord(l)-ord('a')]
            curr[26] = 1
    
    def __init__(self, words: List[str]):
        self.trie = [[] for i in range(27)]
        self.mlength = max([len(w) for w in words])
        self.mem = ''
        self.build_trie(words)

    def query(self, letter: str) -> bool:
        if len(self.mem) < self.mlength:
            self.mem += letter
        else:
            self.mem = self.mem[1:] + letter
        w = self.mem[::-1]
        curr = self.trie
        for l in w:
            if curr[26]:
                return True
            if curr[ord(l)-ord('a')]:
                curr = curr[ord(l)-ord('a')]
            else:
                return False
        if curr[26]:
                return True
        else:
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

