class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.end = \"*\"
        self.q = deque()
        for word in words:
            self.insert(word[::-1])
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node[self.end] = True

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        node = self.root
        for c in self.q:
            if self.end in node: return True
            if c not in node: return False
            
            node = node[c]
        return self.end in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
