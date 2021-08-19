class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            trie = self.trie
            for letter in word[::-1]:
                if letter in trie:
                    trie = trie[letter]
                else:
                    trie[letter] = {}
                    trie = trie[letter]
            trie['$'] = ''
        print((self.trie))
        self.queue = deque()
        self.max_len = max(len(word) for word in words)

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        if len(self.queue) > self.max_len:
            self.queue.pop()
        trie = self.trie
        for letter in self.queue:
            trie = trie.get(letter)
            if trie is None:
                return False
            if '$' in trie:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
