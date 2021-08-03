class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for chrs in word:
                if chrs not in cur:
                    cur[chrs] = {}
                cur = cur[chrs]
            cur['#'] = True
        self.stream = collections.deque()
        print((self.trie))

    def query(self, letter: str) -> bool:
        temp = collections.deque()
        self.stream.append(self.trie)
        for p in self.stream:
            if letter in p:
                temp.append(p[letter])
        self.stream = temp
        for p in self.stream:
            if '#' in p:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
