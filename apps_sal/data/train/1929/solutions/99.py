class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = {}
        
        self.candidates = deque()
    def query(self, letter: str) -> bool:
        size = len(self.candidates)
        for i in range(size):
            candidate = self.candidates.popleft()
            if letter in candidate:
                self.candidates.append(candidate[letter])
        if letter in self.trie:
            self.candidates.append(self.trie[letter])
        for candidate in self.candidates:
            if '#' in candidate:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

