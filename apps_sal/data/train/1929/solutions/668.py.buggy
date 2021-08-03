class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr[\"#\"] = True
        self.pointers = deque()

    def query(self, letter: str) -> bool:
        tmp = deque()
        self.pointers.append(self.trie)
        for p in self.pointers:
            if letter in p:
                tmp.append(p[letter])
        self.pointers = tmp
        for p in self.pointers:
            if \"#\" in p:
                return True
        return False
            
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
