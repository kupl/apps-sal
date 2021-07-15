class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie #root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = True
        self.stream = deque()

    def query(self, letter: str) -> bool:
        temp = deque()
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

